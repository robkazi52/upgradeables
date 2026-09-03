"""Fail CI on semantic boilerplate, incomplete packages, or duplicate mechanisms."""
from __future__ import annotations

import csv
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SECTIONS = (
    "Summary", "Purpose", "Problem Solved", "Where It Fits in the OS",
    "Best-Fit Activities / Tasks", "When Not to Use", "Scope",
    "Trigger Conditions", "Non-Triggers", "Inputs / Required State",
    "Outputs / Produced State", "Mechanism", "Procedure", "Always-Do Rules",
    "Never-Do / Avoid Rules", "Interaction Rules", "Compatible Upgradeables",
    "Counterbalancing Upgradeables", "Potential Redundancy",
    "Conflict / Precedence Rules", "Failure Boundary", "Strong-Model Scaling",
    "Recommended Skill Types", "Example Composition", "Tests",
    "Provenance / Historical Aliases",
)
FORBIDDEN = (
    "prevents the workflow failure implied by the trigger",
    "apply the named behavior as an explicit, bounded control",
    "the declared trigger is absent or the control would add no material value",
    "bounded component result",
)


def section(text, heading):
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def normalize(value):
    return " ".join(re.findall(r"[a-z0-9]+", value.casefold()))


def main():
    errors = []
    signatures = []
    metadata_paths = sorted(ROOT.glob("upgradeables/*/*/metadata.yaml"))
    for metadata_path in metadata_paths:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        slug = metadata["slug"]
        doc = metadata_path.parent / "UPGRADEABLE.md"
        example = metadata_path.parent / "examples/basic.md"
        cases = metadata_path.parent / "tests/cases.json"
        text = doc.read_text(encoding="utf-8") if doc.exists() else ""
        lowered = text.casefold()
        for phrase in FORBIDDEN:
            if phrase in lowered:
                errors.append(f"{slug}: forbidden boilerplate: {phrase}")
        for heading in REQUIRED_SECTIONS:
            body = section(text, heading)
            if len(normalize(body).split()) < 5:
                errors.append(f"{slug}: missing or trivial section {heading}")
        if metadata.get("best_fit_tasks") == ["general-agent-workflow"]:
            errors.append(f"{slug}: generic-only task mapping")
        for key in ("os_role", "pipeline_stages", "best_fit_tasks", "avoid_when", "source_refs"):
            if not isinstance(metadata.get(key), list) or not metadata[key]:
                errors.append(f"{slug}: missing metadata {key}")
        if metadata.get("mechanism_basis") not in {"recovered", "normalized-from-recovered", "modern-interpretation", "provisional"}:
            errors.append(f"{slug}: invalid mechanism_basis")
        if metadata.get("purpose") not in section(text, "Purpose"):
            errors.append(f"{slug}: purpose metadata/document mismatch")
        if metadata.get("mechanism") not in section(text, "Mechanism"):
            errors.append(f"{slug}: mechanism metadata/document mismatch")
        for task in metadata.get("best_fit_tasks", []):
            if task not in section(text, "Best-Fit Activities / Tasks"):
                errors.append(f"{slug}: task mapping missing from documentation: {task}")
        if not example.is_file() or len(normalize(example.read_text(encoding="utf-8")).split()) < 45:
            errors.append(f"{slug}: missing or trivial example")
        if not cases.is_file():
            errors.append(f"{slug}: missing behavior cases")
        combined = normalize(section(text, "Mechanism") + " " + section(text, "Procedure"))
        if len(combined.split()) < 35:
            errors.append(f"{slug}: mechanism/procedure lacks semantic detail")
        signatures.append((slug, combined))

    for index, (left_slug, left) in enumerate(signatures):
        for right_slug, right in signatures[index + 1:]:
            if left == right:
                errors.append(f"exact duplicate mechanism/procedure: {left_slug} and {right_slug}")
            elif min(len(left), len(right)) > 180 and SequenceMatcher(None, left, right).ratio() >= 0.94:
                errors.append(f"near-duplicate mechanism/procedure: {left_slug} and {right_slug}")

    baseline = json.loads((ROOT / "audit/v0.1.0-operational-baseline.json").read_text(encoding="utf-8"))
    baseline_slugs = {item["slug"] for item in baseline["packages"]}
    audit_path = ROOT / "audit/OPERATIONAL_PACKAGE_REVIEW_v0.2.csv"
    if not audit_path.exists():
        errors.append("missing operational package audit")
    else:
        with audit_path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        audit_slugs = {row["slug"] for row in rows}
        if audit_slugs != baseline_slugs:
            errors.append("operational audit does not exactly cover baseline")
        for row in rows:
            if row.get("final_status") not in {"PASS", "BLOCKED_BY_SOURCE_GAP"}:
                errors.append(f"{row.get('slug')}: invalid/unreviewed audit status")
            if any(row.get(key) != "PASS" for key in (
                "summary_review", "purpose_review", "problem_review", "mechanism_review",
                "procedure_review", "trigger_review", "os_fit_review", "task_mapping_review",
                "interaction_review", "example_review", "test_review", "metadata_review",
                "provenance_review", "semantic_specificity",
            )):
                errors.append(f"{row.get('slug')}: incomplete audit checks")
    if errors:
        print("semantic specificity audit: FAILED", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
        return 1
    print(f"semantic specificity audit: OK ({len(metadata_paths)} packages, 0 unreviewed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
