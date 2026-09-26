#!/usr/bin/env python3
from pathlib import Path
import re
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    errors=[]
    status=yaml.safe_load((ROOT/"migration-status-1.5.yaml").read_text(encoding="utf-8"))
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    registry=yaml.safe_load((ROOT/"runtime-distribution-registry.yaml").read_text(encoding="utf-8"))
    tests=yaml.safe_load((ROOT/"tests/TEST-MANIFEST.yaml").read_text(encoding="utf-8"))
    canonical=(ROOT/project["instructions"]["canonical"]).read_bytes()
    legacy=(ROOT/project["instructions"]["legacy_source"]).read_bytes()
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()
    upload=(ROOT/"builder/UPLOAD-MANIFEST.md").read_text(encoding="utf-8").split("## Add in later prompts")[0]
    knowledge=list(dict.fromkeys(re.findall(r"`knowledge/([^`]+\.md)`",upload)))
    readme=(ROOT/"README.md").read_text(encoding="utf-8")

    p=status.get("progress",{})
    if p.get("last_completed_step")!=7:
        errors.append("migration last_completed_step must be 7")
    if p.get("completed_steps")!=list(range(1,8)):
        errors.append("migration completed_steps must be exactly 1..7")
    if status.get("final_readiness",{}).get("migration_steps_complete")!=7:
        errors.append("final readiness must declare 7/7")
    if canonical!=legacy:
        errors.append("canonical and legacy instructions diverged")
    if version!="1.0.0-rc2":
        errors.append(f"VERSION changed: {version!r}")
    if len(knowledge)!=13:
        errors.append(f"expected 13 Knowledge files, found {len(knowledge)}")
    for name in knowledge:
        if not (ROOT/"knowledge"/name).is_file():
            errors.append(f"missing Knowledge file: {name}")

    entries=tests.get("tests",[])
    expected_ids=[f"G{i:02d}" for i in range(1,17)]
    if [x.get("id") for x in entries]!=expected_ids:
        errors.append("G01-G16 test set changed")
    changed=[x.get("id") for x in entries if x.get("status")!="notRun"]
    if changed:
        errors.append(f"migration changed manual Preview status: {changed}")

    if project["release"].get("publication_status")!="private_until_preflight":
        errors.append("project publication status must remain private_until_preflight")
    if registry.get("active_targets")!=["chat","custom-gpt"]:
        errors.append(f"unexpected active targets: {registry.get('active_targets')}")
    for name in ("claude","opencode","openai_plugin"):
        if name not in registry.get("inactive_targets",{}):
            errors.append(f"missing inactive runtime decision: {name}")
    if "7/7 komplett" not in readme:
        errors.append("README does not state completed GPT Builder 1.5 migration")

    critical=[
        "Separate visual quality from technical validity.",
        "Measure actual files.",
        "Use image generation for visual creation or editing and Code Interpreter & Data Analysis for measurable file operations",
        "preserve the original, use the latest complete approved archive as source of truth",
    ]
    text=canonical.decode("utf-8")
    for marker in critical:
        if marker not in text:
            errors.append(f"canonical behavior marker missing: {marker}")

    if errors:
        print("GPT BUILDER 1.5 MIGRATION: FAIL")
        for e in errors: print("-",e)
        return 1
    print("GPT BUILDER 1.5 MIGRATION: PASS")
    print("7/7 complete; VERSION 1.0.0-rc2; 13/13 Knowledge; G01-G16 notRun; privateUntilPreflight preserved")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
