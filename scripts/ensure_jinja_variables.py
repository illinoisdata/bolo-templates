import re
from pathlib import Path

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
DEFAULT_DEVICE = "cuda:0"

TAG_RE = re.compile(r'\{%(-?)\s*(\w+)\s*(.*?)\s*(-?)%\}', re.DOTALL)
ASSIGN_RE = re.compile(r'(\w+)\s*=\s*(.*)', re.DOTALL)
BLOCK_TAGS = {"for", "if", "macro", "call", "filter", "with", "block"}


def make_default(var, val, lstrip="", rstrip=""):
    return f'{{%{lstrip} set {var} = {var} | default({val}) {rstrip}%}}'


def process(path):
    canonical = {
        "repo_id": '"' + path.parent.name.replace("__SEP__", "/") + '"',
        "device": f'"{DEFAULT_DEVICE}"',
    }
    text = path.read_text(encoding="utf-8")
    out, pos, depth, seen, open_block_set = [], 0, 0, set(), False

    for m in TAG_RE.finditer(text):
        lstrip, kw, body, rstrip = m.groups()
        new = m.group(0)
        if kw in BLOCK_TAGS:
            depth += 1
        elif kw.startswith("end") and kw != "endset":
            depth -= 1
        elif kw == "endset" and open_block_set:
            new += "{% endif %}"
            open_block_set = False
        elif kw == "set" and depth == 0:
            assign = ASSIGN_RE.fullmatch(body)
            if assign:
                var, val = assign.groups()
                if var in canonical:
                    new = make_default(var, canonical[var], lstrip, rstrip)
                elif var not in seen and not re.match(rf'{var}\s*\|\s*default\b', val):
                    new = make_default(var, val, lstrip, rstrip)
                seen.add(var)
            elif re.fullmatch(r'\w+', body) and body not in seen:
                new = f'{{%{lstrip} if {body} is not defined %}}' + new
                open_block_set = True
                seen.add(body)
        out.append(text[pos:m.start()] + new)
        pos = m.end()
    text = "".join(out) + text[pos:]

    prepend = [make_default(var, val) for var, val in canonical.items() if var not in seen]
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
