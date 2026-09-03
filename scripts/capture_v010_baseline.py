"""Capture the immutable v0.1.0 operational package baseline once."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "audit/v0.1.0-operational-baseline.json"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write the baseline once")
    args = parser.parse_args()
    entries = []
    for path in sorted(ROOT.glob("upgradeables/*/*/metadata.yaml")):
        item = json.loads(path.read_text(encoding="utf-8"))
        entries.append({
            "slug": item["slug"],
            "id": item["id"],
            "display_name": item["display_name"],
            "version": item["version"],
            "package_path": item["package_path"],
        })
    payload = {
        "release": "v0.1.0",
        "captured_from_commit": "624fc845fc0786775589dfcb29e09035990fe015",
        "operational_package_count": len(entries),
        "packages": entries,
    }
    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if TARGET.exists():
        if TARGET.read_text(encoding="utf-8") != rendered:
            raise SystemExit("existing baseline differs; refusing to overwrite")
        print(f"baseline already captured ({len(entries)} packages)")
        return 0
    if not args.write:
        raise SystemExit("baseline missing; rerun once with --write")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"captured v0.1.0 baseline ({len(entries)} packages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
