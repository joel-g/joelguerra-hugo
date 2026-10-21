"""Build/check in staging, then replace output; failure preserves last good output."""
import argparse
import hashlib
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def retain_versioned(previous, stage):
    """Carry immutable media forward for stale HTML; reject changed hash URLs."""
    folder = previous / 'media' / 'versioned'
    for source in folder.glob('*'):
        if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != source.stem:
            raise ValueError(f'Invalid retained media asset: {source}')
        target = stage / 'media' / 'versioned' / source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and source.read_bytes() != target.read_bytes():
            raise ValueError(f'Immutable URL collision: {source.name}')
        if not target.exists():
            shutil.copy2(source, target)
    for source in (previous / 'assets' / 'versioned').glob('*.css'):
        digest = source.stem.rsplit('.', 1)[-1]
        if hashlib.sha256(source.read_bytes()).hexdigest() != digest:
            raise ValueError(f'Invalid retained stylesheet: {source}')
        target = stage / 'assets' / 'versioned' / source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and source.read_bytes() != target.read_bytes():
            raise ValueError(f'Immutable stylesheet URL collision: {source.name}')
        if not target.exists():
            shutil.copy2(source, target)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hugo', default=os.environ.get('HUGO_BINARY'))
    parser.add_argument('--environment', choices=('production', 'preview'), default='production')
    parser.add_argument('--destination', default='public')
    parser.add_argument('--retain-from', type=Path, help='Previous complete deployment artifact for a clean checkout')
    args = parser.parse_args()
    version = (ROOT / '.hugo-version').read_text().strip()
    binary = args.hugo or str(ROOT / '.tools' / f'hugo-{version}' / ('hugo.exe' if os.name == 'nt' else 'hugo'))
    output = (ROOT / args.destination).resolve()
    allowed = output == ROOT / 'public' or (ROOT / '.build') in output.parents
    if not allowed:
        parser.error('destination must be public or a child of .build within this checkout')
    actual = subprocess.check_output([binary, 'version'], text=True)
    if not re.search(rf'\bv{re.escape(version)}(?:-|\+|\s)', actual) or '+extended' not in actual:
        raise SystemExit(f'Expected Hugo {version} extended; found {actual.strip()}')
    output.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.hugo-stage-', dir=output.parent))
    backup = None
    try:
        subprocess.run([binary, '--destination', str(stage), '--environment', args.environment, '--minify'], cwd=ROOT, check=True)
        retain_versioned(output, stage)
        if args.retain_from:
            if not args.retain_from.is_dir():
                raise ValueError('retain-from must be an existing deployment artifact directory')
            retain_versioned(args.retain_from, stage)
        subprocess.run([os.sys.executable, str(ROOT / 'scripts' / 'verify_site.py'), str(stage), '--environment', args.environment], cwd=ROOT, check=True)
        if output.exists():
            backup = Path(tempfile.mkdtemp(prefix='.hugo-backup-', dir=output.parent))
            backup.rmdir()
            output.rename(backup)
        try:
            stage.rename(output)
        except BaseException:
            if backup is not None:
                backup.rename(output)
            raise
        if backup is not None:
            shutil.rmtree(backup)
        print(f'Validated {args.environment} output: {output}')
    finally:
        if stage.exists():
            shutil.rmtree(stage)

if __name__ == '__main__':
    main()
