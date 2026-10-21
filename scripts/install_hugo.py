"""Fetch the pinned portable Hugo binary; do not change PATH or system settings."""
import hashlib
import io
import platform
import tarfile
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / '.hugo-version').read_text().strip()
ARCHIVES = {
    'Windows': ('windows-amd64.zip', 'de9bd0bee08b336e76863f4c225aa4af0e1c275700f6e2dd0536271f7034dac7'),
    'Linux': ('linux-amd64.tar.gz', '7e0d180a7004519cc794ab76f1c70fa6c9572838528d9787fb13ab4934f4af28'),
}

def main():
    if VERSION != '0.142.0' or platform.machine().lower() not in ('amd64', 'x86_64'):
        raise SystemExit('Review version/checksums or install the pinned Hugo extended for this platform manually.')
    suffix, expected = ARCHIVES[platform.system()]
    archive = f'hugo_extended_{VERSION}_{suffix}'
    url = f'https://github.com/gohugoio/hugo/releases/download/v{VERSION}/{archive}'
    data = urllib.request.urlopen(url, timeout=60).read()
    if hashlib.sha256(data).hexdigest() != expected:
        raise SystemExit('Hugo archive checksum mismatch; nothing installed')
    destination = ROOT / '.tools' / f'hugo-{VERSION}'
    destination.mkdir(parents=True, exist_ok=True)
    name = 'hugo.exe' if platform.system() == 'Windows' else 'hugo'
    if name.endswith('.exe'):
        with zipfile.ZipFile(io.BytesIO(data)) as package:
            binary = package.read(name)
    else:
        with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as package:
            binary = package.extractfile(name).read()
    target = destination / name
    target.write_bytes(binary)
    target.chmod(0o755)
    print(target)

if __name__ == '__main__':
    main()
