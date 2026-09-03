"""Dependency-free structural validation for all behavioral case sets."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_TYPES = {
    "positive_activation", "negative_activation", "precedence_or_conflict",
    "failure_boundary", "strong_model_scaling", "distinctive_mechanism",
}


def main():
    errors = []
    metadata_paths = sorted(ROOT.glob("upgradeables/*/*/metadata.yaml"))
    for metadata_path in metadata_paths:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        path = metadata_path.parent / "tests/cases.json"
        if not path.is_file():
            errors.append(f"{metadata['slug']}: missing tests/cases.json")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("slug") != metadata["slug"]:
            errors.append(f"{metadata['slug']}: behavior slug mismatch")
        if data.get("package_version") != metadata["version"]:
            errors.append(f"{metadata['slug']}: behavior version mismatch")
        cases = data.get("cases")
        if not isinstance(cases, list):
            errors.append(f"{metadata['slug']}: cases must be an array")
            continue
        types = [case.get("type") for case in cases if isinstance(case, dict)]
        if set(types) != REQUIRED_TYPES or len(types) != len(REQUIRED_TYPES):
            errors.append(f"{metadata['slug']}: requires exactly six distinct case types")
        ids = [case.get("id") for case in cases if isinstance(case, dict)]
        if len(ids) != len(set(ids)):
            errors.append(f"{metadata['slug']}: duplicate behavior case ID")
        for case in cases:
            if not isinstance(case, dict):
                errors.append(f"{metadata['slug']}: case must be an object")
                continue
            for key in ("id", "type", "execution", "given", "expect", "reject"):
                if not isinstance(case.get(key), str) or not case[key].strip():
                    errors.append(f"{metadata['slug']}: case has invalid {key}")
            if case.get("execution") not in {"deterministic", "model-required"}:
                errors.append(f"{metadata['slug']}: invalid execution classification")
    if errors:
        print("behavior-case validation: FAILED", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
        return 1
    print(f"behavior-case validation: OK ({len(metadata_paths)} packages, {len(metadata_paths) * 6} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
