"""Exercise the real excerpt partial and image hook in a small Hugo fixture."""
import html
import os
import shutil
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Excerpts(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.values = {}
        self.current = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.current = dict(attrs).get('id')
            if self.current:
                self.values[self.current] = ''

    def handle_endtag(self, tag):
        if tag == 'p':
            self.current = None

    def handle_data(self, text):
        if self.current:
            self.values[self.current] += text


class CardExcerptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        version = (ROOT / '.hugo-version').read_text().strip()
        executable = 'hugo.exe' if os.name == 'nt' else 'hugo'
        binary = os.environ.get('HUGO_BINARY') or str(ROOT / '.tools' / f'hugo-{version}' / executable)
        if not Path(binary).is_file():
            binary = shutil.which(binary)
        if not binary:
            raise unittest.SkipTest('Install pinned Hugo or set HUGO_BINARY to exercise the templates')
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        fixture = Path(cls.temp.name)
        for folder in ('content', 'layouts/partials', 'layouts/_default/_markup'):
            (fixture / folder).mkdir(parents=True)
        (fixture / 'hugo.toml').write_text(
            'baseURL = "https://example.test/"\n'
            'disableKinds = ["taxonomy", "term", "RSS", "sitemap"]\n'
            '[markup.goldmark.renderer]\nunsafe = true\n', encoding='utf-8')
        for path in ('layouts/partials/card-excerpt.html', 'layouts/_default/_markup/render-image.html'):
            shutil.copyfile(ROOT / path, fixture / path)
        # The production image hook emits its real helper link; omit expensive media processing here.
        (fixture / 'layouts/partials/responsive-image.html').write_text(
            '<img src="{{ .src }}" alt="{{ .alt }}">', encoding='utf-8')
        (fixture / 'layouts/index.html').write_text(
            '{{ range .Site.RegularPages }}<p id="{{ .File.ContentBaseName }}">'
            '{{ partial "card-excerpt.html" . }}</p>{{ end }}', encoding='utf-8')
        (fixture / 'layouts/_default/single.html').write_text('{{ .Content }}', encoding='utf-8')
        documents = {
            'generated': 'Caption before the photograph.\n\n![Photograph](/photo.jpg)\n\nUseful caption after the photograph.',
            'multiple': 'Two photographs follow.\n\n![First](/first.jpg)\n\nBetween the photographs.\n\n![Second](/second.jpg)\n\nFinal caption.',
            'legitimate': 'The menu says View original image. [View original image](/manual/) explains the control.',
            'similar-class': '<a class="original-image-credit" href="/credit/">View original image</a> is the credit caption.',
            'other-caption': '<a class="original-image" href="/caption/">Read the meaningful caption</a> remains useful.',
            'encoding': 'Tools & parts cost less than expected. ' + 'A useful sentence. ' * 30,
        }
        for name, body in documents.items():
            (fixture / 'content' / f'{name}.md').write_text(
                f'---\ntitle: "{name}"\n---\n\n{body}\n', encoding='utf-8')
        env = os.environ.copy()
        env['GOMAXPROCS'] = '2'
        subprocess.run([binary, '--source', str(fixture), '--destination', str(fixture / 'public')],
                       env=env, check=True, capture_output=True, text=True)
        cls.output = fixture / 'public'
        cls.raw = (cls.output / 'index.html').read_text(encoding='utf-8')
        cls.excerpts = Excerpts(cls.raw).values

    def test_generated_helper_text_is_excluded_and_captions_survive(self):
        text = self.excerpts['generated']
        self.assertNotIn('View original image', text)
        self.assertIn('Caption before the photograph.', text)
        self.assertIn('Useful caption after the photograph.', text)

    def test_all_generated_helpers_are_excluded(self):
        text = self.excerpts['multiple']
        self.assertNotIn('View original image', text)
        self.assertIn('Between the photographs.', text)
        self.assertIn('Final caption.', text)

    def test_full_article_keeps_original_image_links(self):
        article = (self.output / 'generated/index.html').read_text(encoding='utf-8')
        self.assertIn('class="original-image"', article)
        self.assertIn('href="/photo.jpg">View original image</a>', article)

    def test_legitimate_phrase_and_author_link_text_are_preserved(self):
        self.assertEqual(self.excerpts['legitimate'].count('View original image'), 2)

    def test_similar_class_and_meaningful_caption_are_preserved(self):
        self.assertIn('View original image is the credit caption.', self.excerpts['similar-class'])
        self.assertIn('Read the meaningful caption remains useful.', self.excerpts['other-caption'])

    def test_plaintext_encoding_and_length_remain_bounded(self):
        self.assertIn('Tools & parts', self.excerpts['encoding'])
        self.assertNotIn('&amp;', self.excerpts['encoding'])
        self.assertTrue(all(len(text) <= 220 for text in self.excerpts.values()))
        self.assertNotIn('<a ', html.unescape(self.raw))


if __name__ == '__main__':
    unittest.main()
