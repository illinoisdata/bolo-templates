import sqlite3
from pathlib import Path


def process(teamplte_dir: Path, available_milestones: list[str]):
    post_processed_templates_dir = Path(__file__).parent.parent / "templates"

    for milestone in available_milestones:
        n = milestone[0]
        transformers_db = teamplte_dir / n / "db" / milestone[1]
        others_db = teamplte_dir / n / "db" / milestone[2]

        # transformers README.md
        conn = sqlite3.connect(transformers_db)
        cur = conn.cursor()
        cur.execute("""
            SELECT t.id, r.content
            FROM transformers t
            LEFT JOIN readme r ON r.repo_id = t.id
        """)
        for repo_id, content in cur.fetchall():
            folder = post_processed_templates_dir / repo_id.replace("/", "__SEP__")
            if not folder.exists():
                continue
            (folder / "README.md").write_text(content if content else "", encoding="utf-8")
        conn.close()

        # others README.md
        conn = sqlite3.connect(others_db)
        cur = conn.cursor()
        cur.execute("SELECT id, content FROM others")
        for repo_id, content in cur.fetchall():
            folder = post_processed_templates_dir / repo_id.replace("/", "__SEP__")
            if not folder.exists():
                continue
            (folder / "README.md").write_text(content if content else "", encoding="utf-8")
        conn.close()

        
if __name__ == "__main__":
    TEMPLATE_DIR = Path("/u/yunqili4/scratch/templates")
    available_milestones = [
        ("milestone1", "transformers2.db", "others.db")
    ]
    process(TEMPLATE_DIR, available_milestones)

