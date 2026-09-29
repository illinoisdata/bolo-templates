import re
import sys
from pathlib import Path

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
DEMO_DATA_DIR = TEMPLATES_DIR / "_demo_data"
DATA_PREFIXES = (
    "/u/yli77/projects/ML-code-generation/data/",
    "/u/yunqili4/projects/ML-code-generation/data/",
)
ALLOWED_PREFIXES = ("/tmp/", "/workspace/.pip/")
ABS_PATH_RE = re.compile(r'''["'](/[\w.-]+/[^"'\s]*)''')


def main():
    bad = 0
    for tpl in sorted(TEMPLATES_DIR.glob("*/template.j2")):
        if tpl.parent == DEMO_DATA_DIR:
            continue
        for path in ABS_PATH_RE.findall(tpl.read_text(encoding="utf-8")):
            prefix = next((p for p in DATA_PREFIXES if path.startswith(p)), None)
            if prefix and (DEMO_DATA_DIR / path[len(prefix):]).exists():
                continue
            if not prefix and path.startswith(ALLOWED_PREFIXES):
                continue
            print(f"{tpl.parent.name}: {path}")
            bad += 1
    sys.exit(bad > 0)


if __name__ == "__main__":
    main()
