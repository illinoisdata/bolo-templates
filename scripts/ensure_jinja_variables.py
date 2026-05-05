import re
from pathlib import Path

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
DEFAULT_DEVICE = "cuda:0"

REPO_LINE_RE = re.compile(r'^\{%-?\s*set\s+repo_id\s*=.*?-?%\}\s*$', re.MULTILINE)
DEVICE_LINE_RE = re.compile(r'^\{%-?\s*set\s+device\s*=.*?-?%\}\s*$', re.MULTILINE)
SET_LINE_RE = re.compile(r'^\{%-?\s*set\s+(\w+)\s*=\s*(.*?)\s*-?%\}\s*$', re.MULTILINE)


def make_default(var, val):
    return f'{{% set {var} = {var} | default({val}) %}}'


def process(path):
    repo_id = path.parent.name.replace("__SEP__", "/")
    canonical_repo = make_default("repo_id", f'"{repo_id}"')
    canonical_device = make_default("device", f'"{DEFAULT_DEVICE}"')

    text = path.read_text(encoding="utf-8")
    text, repo_count = REPO_LINE_RE.subn(canonical_repo, text)
    text, device_count = DEVICE_LINE_RE.subn(canonical_device, text)

    def replace_set(m):
        var, val = m.group(1), m.group(2).strip()
        if var in ("repo_id", "device"):
            return m.group(0)
        if "| default" in val or "|default" in val:
            return m.group(0)
        return make_default(var, val)

    text = SET_LINE_RE.sub(replace_set, text)

    prepend = []
    if device_count == 0:
        prepend.append(canonical_device)
    if repo_count == 0:
        prepend.append(canonical_repo)
    if prepend:
        text = "\n".join(prepend) + "\n" + text
    path.write_text(text, encoding="utf-8")


def main():
    for sub in sorted(TEMPLATES_DIR.iterdir()):
        if not sub.is_dir() or sub.name == "_demo_data":
            continue
        tpl = sub / "template.j2"
        if tpl.exists():
            process(tpl)


if __name__ == "__main__":
    main()
