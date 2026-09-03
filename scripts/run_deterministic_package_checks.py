"""Run honest, narrow deterministic checks for packages with lexical/schema logic."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = ROOT / "evals/fixtures/deterministic_package_cases.json"


def no_unresolved_placeholders(data):
    patterns = (
        (r"\{\{[^{}]+\}\}", 0),
        (r"\[[A-Z][A-Z0-9_ -]{2,}\]", 0),
        (r"\[(?:insert|enter|replace|your)\b[^\]\n]*\]", re.IGNORECASE),
        (r"\b(?:TBD|TODO|FIXME)\b", 0),
    )
    return not any(re.search(pattern, data["text"], flags) for pattern, flags in patterns)


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


def validate_fixture(fixture):
    """Reject malformed fixture data before interpreting any expected result."""
    if not isinstance(fixture, dict):
        raise ValueError("fixture must be an object")
    if fixture.get("schema_version") != "1.1.0":
        raise ValueError("fixture schema_version must be 1.1.0")
    cases = fixture.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("fixture cases must be a non-empty list")
    seen_ids = set()
    for index, case in enumerate(cases):
        label = f"case {index + 1}"
        if not isinstance(case, dict):
            raise ValueError(f"{label} must be an object")
        missing = {"id", "package", "check", "input", "expected"} - set(case)
        if missing:
            raise ValueError(f"{label} missing fields: {', '.join(sorted(missing))}")
        if not isinstance(case["id"], str) or not case["id"].strip():
            raise ValueError(f"{label} id must be a non-empty string")
        if case["id"] in seen_ids:
            raise ValueError(f"duplicate case id: {case['id']}")
        seen_ids.add(case["id"])
        if case["check"] not in CHECKS:
            raise ValueError(f"{case['id']}: unknown check {case['check']!r}")
        if not isinstance(case["input"], dict):
            raise ValueError(f"{case['id']}: input must be an object")
        if type(case["expected"]) is not bool:
            raise ValueError(f"{case['id']}: expected must be boolean")
    return cases


def evaluate_fixture(fixture):
    cases = validate_fixture(fixture)
    failures = []
    for case in cases:
        try:
            actual = CHECKS[case["check"]](case["input"])
        except (KeyError, TypeError) as exc:
            failures.append(f"{case['id']}: invalid input ({exc})")
            continue
        if actual is not case["expected"]:
            failures.append(
                f"{case['id']} ({case['package']}/{case['check']}): "
                f"expected {case['expected']}, got {actual}"
            )
    return failures


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    args = parser.parse_args(argv)
    try:
        fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
        failures = evaluate_fixture(fixture)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"deterministic package checks: INVALID FIXTURE ({exc})", file=sys.stderr)
        return 2
    if failures:
        print("deterministic package checks: FAILED", file=sys.stderr)
        for failure in failures:
            print("- " + failure, file=sys.stderr)
        return 1
    print(f"deterministic package checks: OK ({len(fixture['cases'])} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
