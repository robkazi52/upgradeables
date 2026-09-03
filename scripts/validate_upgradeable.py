"""Validate one JSON-compatible metadata.yaml package."""
import json
import re
import sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("usage: validate_upgradeable.py path/to/metadata.yaml", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    required = {"id", "slug", "display_name", "version", "registry_generation", "recovery_status", "lifecycle_status", "functional_classes", "activation_class", "implementation_forms", "purpose", "triggers", "non_triggers", "requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts", "inputs", "outputs", "strong_model_scaling", "failure_boundary", "supersedes", "superseded_by", "package_path", "provenance"}
    missing = required - set(data)
    array_fields = {"functional_classes", "implementation_forms", "triggers", "non_triggers", "requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts", "inputs", "outputs", "failure_boundary", "supersedes", "superseded_by"}
    bad_arrays = sorted(key for key in array_fields if not isinstance(data.get(key), list))
    bad = bool(missing or bad_arrays or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", data.get("slug", "")) or not re.fullmatch(r"\d+\.\d+\.\d+", data.get("version", "")))
    if bad:
        print(f"invalid metadata; missing={sorted(missing)} bad_arrays={bad_arrays}", file=sys.stderr)
        return 1
    print(f"{data['slug']}: OK")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
