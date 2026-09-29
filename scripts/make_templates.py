import json
import shutil
import argparse
from pathlib import Path


TEMPLATES_DIR = Path("/u/yunqili4/scratch/templates")
TEMPLATES_DES = Path(__file__).parents[1] / "templates"


def ensure_des_clean():
    for iterr in TEMPLATES_DES.iterdir():
        if iterr.is_dir() and iterr.name != "_demo_data":
            shutil.rmtree(iterr, ignore_errors=True)


def copy_a_repo_dir(repo_dir_name: str, repo_dir: Path):
    new_repo_dir = TEMPLATES_DES / repo_dir_name
    new_repo_dir.mkdir()
    for file_name in {"template.j2", "requirements.txt"}:
        shutil.copyfile(repo_dir / file_name, new_repo_dir / file_name)


def copy_checkpoint(templates_dir: Path, manifest: dict, ttpye: str, task: str = ""):
    ckpt_file = templates_dir / "_checkpoint" / "checkpoint_001.jsonl"
    with open(ckpt_file, 'r') as ckptf:
        for line in ckptf:
            rec = json.loads(line)
            repo_id, status = rec["repo_id"], rec["validation_ok"]
            if not status:
                continue

            if repo_id in manifest:
                raise KeyError(f"manifest has a key collision : {repo_id}")
            if ttpye == "typeI":
                manifest[repo_id] = {
                    "repo_id": repo_id, 
                    "type": "typeI", 
                    "extra_info": {
                        "task": task, 
                        "pipeline_ok": False
                    }
                }
            else:
                manifest[repo_id] = {
                    "repo_id": repo_id, 
                    "type": "typeII", 
                    "extra_info": {}
                }

            repo_dir_name = "__SEP__".join(repo_id.split('/'))
            repo_dir = templates_dir / repo_dir_name
            copy_a_repo_dir(repo_dir_name, repo_dir)


def copy_typeI(typeI_templates_dir: Path, typeI_llm: str, manifest: dict):
    for task_dir in typeI_templates_dir.iterdir():
        if not task_dir.is_dir():
            continue

        task_base_dir = task_dir / "base"
        task_templates_dir = task_dir / typeI_llm

        base_ckpt_file = task_base_dir / "checkpoint_001.jsonl"
        with open(base_ckpt_file, 'r') as ckptf:
            for line in ckptf:
                rec = json.loads(line)
                repo_id, status = rec["repo_id"], rec["validation_status"]
                if status == "success":
                    manifest[repo_id] = {
                        "repo_id": repo_id, 
                        "type": "typeI", 
                        "extra_info": {
                            "task": task_dir.name, 
                            "pipeline_ok": True
                        }
                    }

        copy_checkpoint(
            task_templates_dir, 
            manifest, 
            ttpye="typeI", 
            task=task_dir.name
        )


def add_behavior_verifications(manifest: dict, ckpt_file: Path):
    with open(ckpt_file, 'r') as ckptf:
        for line in ckptf:
            rec = json.loads(line)
            repo_id = rec["repo_id"]
            manifest[repo_id].update({
                "behavior_status": rec["status"],
                "behavior_reason": rec["reason"]
            })


def add_content_vefifications(manifest: dict, ckpt_file: Path):
    with open(ckpt_file, 'r') as ckptf:
        recs = json.load(ckptf)
        for rec in recs.values():
            repo_id = rec["repo_id"]
            findings = []
            for r in rec["findings"]:
                if r["violated"]:
                    findings.append(r)
            manifest[repo_id].update({
                "content_status": rec["status"],
                "content_findings": findings
            })


def add_verifications(manifest: dict, typeI_llm: str, typeII_llm: str, judge_llm: str):
    judge_archive_dir = TEMPLATES_DIR / "judge-archives"
    typeI_behavior_ckpt_file = judge_archive_dir / f"judge.typeI.{typeI_llm}.{judge_llm}.jsonl"
    typeI_content_ckpt_file = judge_archive_dir / f"deviations.typeI.{typeI_llm}.{judge_llm}.json"
    typeII_behavior_ckpt_file = judge_archive_dir / f"judge.typeII.{typeII_llm}.{judge_llm}.jsonl"
    typeII_content_ckpt_file = judge_archive_dir / f"deviations.typeII.{typeII_llm}.{judge_llm}.json"

    add_behavior_verifications(manifest, typeI_behavior_ckpt_file)
    add_behavior_verifications(manifest, typeII_behavior_ckpt_file)
    add_content_vefifications(manifest, typeI_content_ckpt_file)
    add_content_vefifications(manifest, typeII_content_ckpt_file)


def dump_manifest(manifest: dict):
    manifest_path = TEMPLATES_DES / "manifest.jsonl"
    with open(manifest_path, 'w') as manif:
        for _, rec in manifest.items():
            manif.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main(typeI_llm: str, typeII_llm: str, judge_llm: str):
    typeI_templates_dir = TEMPLATES_DIR / "typeI"
    typeII_templates_dir = TEMPLATES_DIR / "typeII" / typeII_llm
    manifest = {}

    ensure_des_clean()
    copy_typeI(typeI_templates_dir, typeI_llm, manifest)
    copy_checkpoint(typeII_templates_dir, manifest, ttpye="typeII")
    add_verifications(manifest, typeI_llm, typeII_llm, judge_llm)
    dump_manifest(manifest)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--typeI_llm", type=str, required=True)
    parser.add_argument("--typeII_llm", type=str, required=True)
    parser.add_argument("--judge_llm", type=str, required=True)
    args = parser.parse_args()

    main(args.typeI_llm, args.typeII_llm, args.judge_llm)