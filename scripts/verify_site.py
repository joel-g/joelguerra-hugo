"""Offline output checks. External URLs are deliberately not fetched."""
import argparse
import fnmatch
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ORIGIN = 'https://joelguerra.com'

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.main = False
        self.main_tags = []
        self.excerpts = []
        self.excerpt = None
        self.anchor_depth = 0
        self.nested_anchor = False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == 'main':
            self.main = True
        if self.main:
            self.main_tags.append(tag)
        if tag == 'a':
            self.anchor_depth += 1
            self.nested_anchor |= self.anchor_depth > 1
        if tag == 'p' and attrs.get('class') in ('f5 lh-copy','f6 f5-l lh-copy'):
            self.excerpt = ''
    def handle_endtag(self, tag):
        if tag == 'main':
            self.main = False
        if tag == 'a':
            self.anchor_depth = max(0,self.anchor_depth-1)
        if tag == 'p' and self.excerpt is not None:
            self.excerpts.append(self.excerpt)
            self.excerpt = None
    def handle_data(self, data):
        if self.excerpt is not None:
            self.excerpt += data
    def values(self, tag, attr, value, result):
        return [a.get(result, '') for t, a in self.tags if t == tag and a.get(attr) == value]

def header_rules(text):
    rules = []
    for line in text.splitlines():
        if line.startswith('/'):
            rules.append([line.strip(), ''])
        elif line.strip().lower().startswith('cache-control:'):
            rules[-1][1] = line.split(':', 1)[1].strip()
    return rules

def validate(site, environment='production'):
    errors = []
    routes = set()
    rules = header_rules((site / '_headers').read_text())
    if len(rules) > 100:
        errors.append('Cloudflare Pages allows at most 100 header rules')
    allowed = json.loads((ROOT / 'tests' / 'known-local-references.json').read_text())
    known = {(x['page'], x['target']) for x in allowed}
    for file in site.rglob('*.html'):
        relative = file.relative_to(site).as_posix()
        route = '/' + (relative[:-10] if relative.endswith('index.html') else relative)
        routes.add(route)
        doc = Document(file.read_text(encoding='utf-8'))
        redirect = bool(doc.values('meta', 'http-equiv', 'refresh', 'content'))
        if doc.nested_anchor:
            errors.append(f'{route}: nested anchors')
        if not redirect and route != '/404.html':
            expected = ORIGIN + route
            if doc.values('link', 'rel', 'canonical', 'href') != [expected]:
                errors.append(f'{route}: canonical must be exactly {expected}')
            if doc.values('meta', 'property', 'og:url', 'content') != [expected]:
                errors.append(f'{route}: og:url must match canonical')
            robots = doc.values('meta', 'name', 'robots', 'content')
            expected_robots = 'index, follow' if environment == 'production' else 'noindex, nofollow'
            if robots != [expected_robots]:
                errors.append(f'{route}: incorrect {environment} robots meta: {robots}')
            if len([t for t,a in doc.tags if t == 'h1']) != 1:
                errors.append(f'{route}: expected exactly one h1')
            if not doc.values('meta', 'name', 'description', 'content'):
                errors.append(f'{route}: missing description')
            if not doc.values('a','href','#main-content','href') or not doc.values('main','id','main-content','id'):
                errors.append(f'{route}: skip link/target missing')
        if route in ('/','/cars/','/cars/page/2/','/tech/','/tags/honda/'):
            if set(doc.main_tags) & {'table','iframe','video'}:
                errors.append(f'{route}: rich article content leaked into listing')
            if not doc.excerpts or any(len(x)>220 for x in doc.excerpts):
                errors.append(f'{route}: listing excerpt missing/too long')
        for tag, attrs in doc.tags:
            refs = [attrs[k] for k in ('href','src','poster') if k in attrs]
            if 'srcset' in attrs:
                refs.extend(x.strip().split()[0] for x in attrs['srcset'].split(',') if x.strip())
            for ref in refs:
                url = urlsplit(urljoin(ORIGIN + route, ref))
                if url.netloc != 'joelguerra.com' or url.scheme not in ('http','https'):
                    continue
                target = unquote(url.path)
                candidate = site / target.lstrip('/')
                if not candidate.is_file() and not (candidate / 'index.html').is_file() and (route,target) not in known:
                    errors.append(f'{route}: missing local reference {target}')
            if tag == 'img' and '/media/versioned/' in attrs.get('src',''):
                if not all(attrs.get(k) for k in ('width','height','loading')):
                    errors.append(f'{route}: derivative lacks dimensions/loading')
                if 'alt' not in attrs:
                    errors.append(f'{route}: image lacks alt attribute')
        matches = [value for pattern,value in rules if fnmatch.fnmatchcase(route, pattern)]
        if len(matches) != 1 or 'max-age=0' not in matches[0] or 'immutable' in matches[0]:
            errors.append(f'{route}: HTML must match one revalidation cache rule: {matches}')
    expected_routes = set(json.loads((ROOT / 'tests' / 'baseline-routes.json').read_text()))
    if not expected_routes.issubset(routes):
        errors.append(f'preserved routes missing: {sorted(expected_routes-routes)}')
    for source in (ROOT / 'content').rglob('*.md'):
        text = source.read_text(encoding='utf-8')
        frontmatter = text.split('---',2)[1] if text.startswith('---') else ''
        if re.search(r'^draft:\s*true\s*$',frontmatter,re.M|re.I):
            slug_match = re.search(r'^slug:\s*[\x22\x27]?([^\n\x22\x27]+)',frontmatter,re.M)
            slug = slug_match.group(1).strip() if slug_match else source.stem
            route = '/' + source.relative_to(ROOT/'content').parent.as_posix().strip('./') + '/' + slug + '/'
            if route in routes:
                errors.append(f'draft published: {route}')
    for file in (site / 'media' / 'versioned').glob('*'):
        if hashlib.sha256(file.read_bytes()).hexdigest() != file.stem:
            errors.append(f'{file.name}: media name is not its content SHA256')
    for file in (site / 'assets' / 'versioned').glob('*.css'):
        if hashlib.sha256(file.read_bytes()).hexdigest() != file.stem.rsplit('.',1)[-1]:
            errors.append(f'{file.name}: stylesheet name is not its content SHA256')
    for path,digest in json.loads((ROOT/'tests'/'legacy-assets.json').read_text()).items():
        file = site / path.lstrip('/')
        if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest() != digest:
            errors.append(f'{path}: legacy immutable artifact changed or disappeared')
    for file in site.rglob('*'):
        if not file.is_file():
            continue
        path = '/' + file.relative_to(site).as_posix()
        matches = [value for pattern,value in rules if fnmatch.fnmatchcase(path,pattern)]
        if len(matches) > 1:
            errors.append(f'{path}: overlapping Cache-Control rules')
        if matches and 'immutable' in matches[0] and not path.startswith(('/assets/versioned/', '/media/versioned/', '/dist/')):
            errors.append(f'{path}: unversioned immutable asset')
    robots = (site / 'robots.txt').read_text()
    if environment == 'preview' and 'Disallow: /' not in robots:
        errors.append('preview robots must disallow crawling')
    if environment == 'production' and re.search(r'Disallow:\s*/\s*$',robots,re.M):
        errors.append('production robots unexpectedly disallows entire site')
    return sorted(set(errors))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('site', type=Path)
    parser.add_argument('--environment', choices=('production','preview'), default='production')
    args = parser.parse_args()
    errors = validate(args.site, args.environment)
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS offline routes, local references, metadata, media hashes and cache rules ({args.environment})')

if __name__ == '__main__':
    main()
