import re
from pathlib import Path

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"

MAIN_GUARD_RE = re.compile(r'\n*^if __name__\s*==\s*["\']__main__["\']\s*:.*\Z', re.DOTALL | re.MULTILINE)
OUTPUT_DIR_LINE_RE = re.compile(r'^.*\boutput_dir\b.*$\n?', re.MULTILINE)
MULTI_BLANK_RE = re.compile(r'\n{3,}')


def process(path):
    text = path.read_text(encoding="utf-8")
    text = MAIN_GUARD_RE.sub("", text)
    text = OUTPUT_DIR_LINE_RE.sub("", text)
    text = MULTI_BLANK_RE.sub("\n\n", text)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def main():
    for sub in sorted(TEMPLATES_DIR.iterdir()):
        if not sub.is_dir() or sub.name == "_demo_data":
            continue
        tpl = sub / "template.j2"
        if tpl.exists():
            process(tpl)


if __name__ == "__main__":
    main()
