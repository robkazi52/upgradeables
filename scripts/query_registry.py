"""Query the compact Upgradeables catalog and emit JSON."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "registry/catalog.json"


def load_catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def searchable_text(item):
    values = [item["slug"], item["display_name"], item["purpose"]]
    values.extend(item.get("triggers", []))
    values.extend(item.get("functional_classes", []))
    values.extend(item.get("keywords", []))
    return " ".join(values).casefold()


def main():
    parser = argparse.ArgumentParser(
        description="Find Upgradeables or resolve a task recipe. Output is JSON."
    )
    selectors = parser.add_mutually_exclusive_group(required=True)
    selectors.add_argument("--slug", help="exact Upgradeable slug")
    selectors.add_argument("--recipe", help="exact recipe slug with resolved components")
    selectors.add_argument("--class", dest="functional_class", help="functional class")
    selectors.add_argument("--search", help="case-insensitive text/trigger search")
    args = parser.parse_args()
    data = load_catalog()

    if args.slug:
        result = next((item for item in data["upgradeables"] if item["slug"] == args.slug), None)
    elif args.recipe:
        result = next((item for item in data["recipes"] if item["slug"] == args.recipe), None)
    elif args.functional_class:
        result = [
            item for item in data["upgradeables"]
            if args.functional_class in item["functional_classes"]
        ]
    else:
        term = args.search.casefold()
        result = [item for item in data["upgradeables"] if term in searchable_text(item)]

    if result is None:
        print(json.dumps({"error": "not found"}, indent=2), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
