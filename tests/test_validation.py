import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

verify = load('verify_site')
build = load('build')
HTML = '''<html><head><link rel="canonical" href="https://joelguerra.com/">
<meta property="og:url" content="https://joelguerra.com/">
<meta name="robots" content="index, follow"><meta name="description" content="Example"></head>
<body><a href="#main-content">Skip</a><main id="main-content"><h1>Example</h1><p class="f5 lh-copy">Excerpt.</p></main></body></html>'''

class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.site = self.root/'public'
        self.site.mkdir()
        (self.root/'tests').mkdir()
        (self.root/'content').mkdir()
        (self.root/'tests'/'baseline-routes.json').write_text('["/"]')
        (self.root/'tests'/'known-local-references.json').write_text('[]')
        (self.root/'tests'/'legacy-assets.json').write_text('{}')
        (self.site/'index.html').write_text(HTML)
        (self.site/'robots.txt').write_text('User-agent: *\nDisallow:\n')
        (self.site/'_headers').write_text('/\n  Cache-Control: public, max-age=0, must-revalidate\n')
        self.patcher = patch.object(verify,'ROOT',self.root)
        self.patcher.start()
    def tearDown(self):
        self.patcher.stop()
        self.temp.cleanup()
    def test_valid(self):
        self.assertEqual(verify.validate(self.site),[])
    def test_broken_local_reference(self):
        (self.site/'index.html').write_text(HTML.replace('</main>','<img src="/missing.jpg"></main>'))
        self.assertTrue(any('missing local reference /missing.jpg' in x for x in verify.validate(self.site)))
    def test_wrong_canonical(self):
        (self.site/'index.html').write_text(HTML.replace('rel="canonical" href="https://joelguerra.com/"','rel="canonical" href="https://joelguerra.com/wrong/"'))
        self.assertTrue(any('canonical must' in x for x in verify.validate(self.site)))
    def test_preview_cannot_index(self):
        self.assertTrue(any('robots' in x for x in verify.validate(self.site,'preview')))
    def test_cache_overlap(self):
        with (self.site/'_headers').open('a') as out:
            out.write('/*\n  Cache-Control: public, max-age=31536000, immutable\n')
        self.assertTrue(any('overlapping' in x or 'one revalidation' in x for x in verify.validate(self.site)))
    def test_nested_image_link(self):
        doc = verify.Document('<a href="/article/"><picture><img src="/x"></picture><a href="/x">Original</a></a>')
        self.assertTrue(doc.nested_anchor)
    def test_rich_excerpt(self):
        (self.site/'index.html').write_text(HTML.replace('</main>','<table><tr><td>Specs</td></tr></table></main>'))
        self.assertTrue(any('rich article' in x for x in verify.validate(self.site)))
    def test_hash_name_tamper(self):
        folder = self.site/'media'/'versioned';folder.mkdir(parents=True)
        (folder/('0'*64+'.webp')).write_bytes(b'changed')
        self.assertTrue(any('content SHA256' in x for x in verify.validate(self.site)))
    def test_old_derivatives_retained_and_tampering_rejected(self):
        old = self.root/'previous';stage=self.root/'stage'
        folder=old/'media'/'versioned';folder.mkdir(parents=True)
        data=b'previous immutable representation';name=hashlib.sha256(data).hexdigest()+'.webp'
        (folder/name).write_bytes(data)
        build.retain_versioned(old,stage)
        self.assertEqual((stage/'media'/'versioned'/name).read_bytes(),data)
        (folder/name).write_bytes(b'overwrite at same name')
        with self.assertRaises(ValueError):
            build.retain_versioned(old,stage)
    def test_stylesheet_only_previous_artifact(self):
        old=self.root/'previous';stage=self.root/'stage'
        folder=old/'assets'/'versioned';folder.mkdir(parents=True)
        data=b'body{color:#111}';name='site.'+hashlib.sha256(data).hexdigest()+'.css'
        (folder/name).write_bytes(data)
        build.retain_versioned(old,stage)
        self.assertEqual((stage/'assets'/'versioned'/name).read_bytes(),data)

if __name__ == '__main__':
    unittest.main()
