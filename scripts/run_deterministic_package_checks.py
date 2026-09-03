"""Run honest, narrow deterministic checks for packages with lexical/schema logic."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def no_unresolved_placeholders(data):
    patterns = (r"\{\{[^{}]+\}\}", r"\[[A-Z][A-Z0-9_ -]{2,}\]", r"\b(?:TBD|TODO|FIXME)\b")
    return not any(re.search(pattern, data["text"]) for pattern in patterns)


def required_stateblock_fields(data):
    return {"task", "phase", "constraints", "decisions", "open_items"} <= set(data["state"])


def required_snapshot_fields(data):
    return {"version", "task", "phase", "locked_facts", "next_action"} <= set(data["snapshot"])


def locked_literals_preserved(data):
    return all(value in data["before"] and value in data["after"] for value in data["locked"])


def exact_quote_exists(data):
    return data["quote"] in data["source"]


def task_lock_complete(data):
    lock = data["lock"]
    return {"objective", "deliverable", "constraints", "done_when"} <= set(lock) and all(lock[key] for key in lock)


CHECKS = {name: value for name, value in globals().copy().items() if callable(value) and name in {
    "no_unresolved_placeholders", "required_stateblock_fields", "required_snapshot_fields",
    "locked_literals_preserved", "exact_quote_exists", "task_lock_complete",
}}


def main():
    fixture = json.loads((ROOT / "evals/fixtures/deterministic_package_cases.json").read_text(encoding="utf-8"))
    failures = []
    for case in fixture["cases"]:
        actual = CHECKS[case["check"]](case["input"])
        if actual is not case["expected"]:
            failures.append(f"{case['package']}/{case['check']}: expected {case['expected']}, got {actual}")
    if failures:
        print("deterministic package checks: FAILED", file=sys.stderr)
        for failure in failures:
            print("- " + failure, file=sys.stderr)
        return 1
    print(f"deterministic package checks: OK ({len(fixture['cases'])} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
