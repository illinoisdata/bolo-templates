from pathlib import Path

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
PYBOLO_LINE = "pybolo"


def process(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if any(line.startswith(PYBOLO_LINE) for line in lines):
        return
    lines.append(PYBOLO_LINE)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    for sub in sorted(TEMPLATES_DIR.iterdir()):
        if not sub.is_dir() or sub.name == "_demo_data":
            continue
        req = sub / "requirements.txt"
        if req.exists():
            process(req)


if __name__ == "__main__":
    main()
