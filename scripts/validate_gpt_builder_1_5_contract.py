#!/usr/bin/env python3
from pathlib import Path
import re
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    errors=[]
    contract=yaml.safe_load((ROOT/"gpt-builder-1.5-contract.yaml").read_text(encoding="utf-8"))
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    tests=yaml.safe_load((ROOT/"tests/TEST-MANIFEST.yaml").read_text(encoding="utf-8"))
    canonical=(ROOT/project["instructions"]["canonical"]).read_bytes()
    legacy=(ROOT/project["instructions"]["legacy_source"]).read_bytes()
    instruction_text=canonical.decode("utf-8")
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()

    upload=(ROOT/"builder/UPLOAD-MANIFEST.md").read_text(encoding="utf-8").split("## Add in later prompts")[0]
    knowledge=list(dict.fromkeys(re.findall(r"`knowledge/([^`]+\.md)`",upload)))

    if contract["builder"]["target_version"]!="1.5.0":
        errors.append("target builder version must be 1.5.0")
    if contract["builder"]["behavior_preserving"] is not True:
        errors.append("migration must remain behavior-preserving")
    if canonical!=legacy:
        errors.append("canonical and legacy instruction must remain byte-identical during migration")
    if version!="1.0.0-rc2":
        errors.append(f"VERSION changed during migration: {version!r}")
    if len(knowledge)!=13:
        errors.append(f"expected exactly 13 Knowledge files, found {len(knowledge)}")
    for name in knowledge:
        if not (ROOT/"knowledge"/name).is_file():
            errors.append(f"missing Knowledge file: {name}")

    entries=tests.get("tests",[])
    if len(entries)!=16:
        errors.append(f"expected 16 manual Preview tests, found {len(entries)}")
    expected_ids=[f"G{i:02d}" for i in range(1,17)]
    actual_ids=[x.get("id") for x in entries]
    if actual_ids!=expected_ids:
        errors.append(f"manual Preview test IDs changed: {actual_ids}")
    changed=[x.get("id") for x in entries if x.get("status")!="notRun"]
    if changed:
        errors.append(f"migration must not change manual Preview status from notRun: {changed}")

    required_markers=[
        "Separate visual quality from technical validity.",
        "Measure actual files.",
        "Use image generation for visual creation or editing and Code Interpreter & Data Analysis for measurable file operations",
        "preserve the original, use the latest complete approved archive as source of truth",
        "Never claim that a capability ran when it was unavailable or not used.",
    ]
    for marker in required_markers:
        if marker not in instruction_text:
            errors.append(f"canonical instruction missing critical behavior marker: {marker}")

    behavior=contract["behavior"]
    if behavior["exact_file_properties_require_actual_measurement"] is not True:
        errors.append("actual measurement must remain required for exact file properties")
    if behavior["no_false_runtime_integration_claims"] is not True:
        errors.append("false runtime integration claims must remain forbidden")
    if behavior["original_zip_must_not_be_overwritten"] is not True:
        errors.append("original zip preservation must remain required")

    preflight=contract["manual_preflight"]
    if preflight["required_before_publication"] is not True:
        errors.append("manual preflight must remain required before publication")
    if preflight["publication_status"]!="privateUntilPreflight":
        errors.append("publication status must remain privateUntilPreflight")
    if preflight["migration_may_mark_pass"] is not False:
        errors.append("migration may not mark Preview tests as pass")
    if preflight["migration_may_publish"] is not False:
        errors.append("migration may not publish the GPT")

    if errors:
        print("GPT BUILDER 1.5 CONTRACT: FAIL")
        for e in errors: print("-",e)
        return 1

    print("GPT BUILDER 1.5 CONTRACT: PASS")
    print("VERSION 1.0.0-rc2; 13/13 Knowledge; G01-G16 notRun; publication privateUntilPreflight")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
