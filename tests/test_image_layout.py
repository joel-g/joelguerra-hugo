"""Check the explicit responsive sizing contract against article/card markup.

This checks selector coverage, not browser layout or the complete CSS cascade.
"""
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

class Images(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.stack = []
        self.images = []
        self.stylesheets = []
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        node = (tag, dict(attrs))
        if tag == 'img':
            self.images.append((node,list(self.stack)))
        if tag == 'link' and node[1].get('rel') == 'stylesheet':
            self.stylesheets.append(node[1]['href'])
        if tag not in VOID:
            self.stack.append(node)
    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

def matches(selector, image, ancestors):
    def node_matches(part, node):
        tag, attrs = node
        if part.startswith('.'):
            return part[1:] in attrs.get('class','').split()
        return part == tag
    parts = re.split(r'\s*>\s*|\s+',selector.strip())
    if len(parts) == 1:
        return node_matches(parts[0],image)
    if len(parts) == 2 and node_matches(parts[1],image):
        parents = ancestors[-1:] if '>' in selector else ancestors
        return any(node_matches(parts[0],node) for node in parents)
    return False

def uncovered_images(html, css):
    selectors = []
    for selector,body in re.findall(r'([^{}]+)\{([^{}]+)\}',css):
        declarations = dict(part.strip().split(':',1) for part in body.split(';') if ':' in part)
        if declarations.get('height') == 'auto' and declarations.get('max-width') == '100%':
            selectors.extend(selector.split(','))
    return [image[1].get('src','') for image,parents in Images(html).images
            if 'width' in image[1] and 'height' in image[1]
            and not any(matches(selector,image,parents) for selector in selectors)]

class ImageLayoutTests(unittest.TestCase):
    def setUp(self):
        self.css = (ROOT/'assets/css/maintenance.css').read_text()
        self.article = '<div class="nested-img nested-copy-line-height"><picture><source type="image/webp"><img class="responsive-image" src="photo.jpg" width="4000" height="3000"></picture></div>'
        self.card = '<a class="db grow"><picture><source type="image/webp"><img class="img" src="thumbnail.jpg" width="4000" height="3000"></picture></a>'
    def test_article_and_card_intrinsic_dimensions_allow_auto_height(self):
        self.assertEqual(uncovered_images(self.article+self.card,self.css),[])
    def test_obsolete_article_selector_is_rejected(self):
        obsolete = '.article-body img{height:auto;max-width:100%}'
        self.assertEqual(uncovered_images(self.article+self.card,obsolete),['photo.jpg','thumbnail.jpg'])
    def test_generated_output_images_have_matching_sizing_rule(self):
        output = ROOT/'public'
        if not (output/'index.html').exists():
            self.skipTest('Build output first to check actual generated markup')
        count = 0
        stylesheets = {}
        for page in output.rglob('*.html'):
            html = page.read_text(encoding='utf-8')
            document = Images(html)
            count += len(document.images)
            css = ''
            for href in document.stylesheets:
                if href not in stylesheets:
                    file = output/unquote(urlsplit(href).path).lstrip('/')
                    stylesheets[href] = file.read_text(encoding='utf-8')
                css += stylesheets[href]
            self.assertEqual(uncovered_images(html,css),[],str(page.relative_to(output)))
        self.assertGreater(count,0)

if __name__ == '__main__':
    unittest.main()
