"""Run provider-neutral Upgradeable behavior cases through an explicit adapter."""
from __future__ import annotations

import argparse
import json
import shlex
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evals.adapters.command import CommandAdapter  # noqa: E402
from evals.adapters.mock import MockAdapter  # noqa: E402


def load_case_sets(slugs: list[str]):
    paths = sorted(ROOT.glob("upgradeables/*/*/tests/cases.json"))
    if slugs:
        wanted = set(slugs)
        paths = [path for path in paths if path.parent.parent.name in wanted]
        found = {path.parent.parent.name for path in paths}
        missing = wanted - found
        if missing:
            raise ValueError(f"unknown package slug(s): {', '.join(sorted(missing))}")
    return [(path.parent.parent, json.loads(path.read_text(encoding="utf-8"))) for path in paths]


def load_judgments(path: Path | None):
    if path is None:
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("judgments must be an object keyed by case ID")
    for case_id, value in data.items():
        if not isinstance(value, dict) or value.get("outcome") not in {"pass", "fail", "uncertain"}:
            raise ValueError(f"{case_id}: judgment needs outcome pass, fail, or uncertain")
    return data


def case_prompt(package_dir: Path, case: dict):
    instructions = (package_dir / "UPGRADEABLE.md").read_text(encoding="utf-8")
    return (
        "Follow host and user authority. Use the following optional Upgradeable only "
        "when its documented trigger is active. Complete the case itself; do not discuss "
        "the evaluation rubric.\n\n"
        f"--- UPGRADEABLE ---\n{instructions}\n\n"
        f"--- CASE ({case['type']}) ---\n{case['given']}\n"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--adapter", choices=("mock", "command"), required=True)
    parser.add_argument("--command", help="Local model command; parsed without a shell")
    parser.add_argument("--allow-mock", action="store_true", help="Acknowledge mock output is not evidence")
    parser.add_argument("--mock-response", default="MOCK RESPONSE - NOT A MODEL RESULT")
    parser.add_argument("--package", action="append", default=[], help="Package slug; repeat to select several")
    parser.add_argument("--case-type", action="append", default=[], help="Behavior case type; repeat to select")
    parser.add_argument("--max-cases", type=int)
    parser.add_argument("--model", required=True, help="Exact model/build label, or mock")
    parser.add_argument("--parameters", default="{}", help="JSON object describing inference parameters")
    parser.add_argument("--judgments", type=Path, help="Optional JSON judgments keyed by case ID")
    destination = parser.add_mutually_exclusive_group(required=True)
    destination.add_argument("--output", type=Path, help="Report JSON path")
    destination.add_argument("--stdout", action="store_true", help="Write report JSON to stdout")
    args = parser.parse_args()

    if args.max_cases is not None and args.max_cases < 1:
        parser.error("--max-cases must be positive")
    try:
        parameters = json.loads(args.parameters)
        if not isinstance(parameters, dict):
            raise ValueError("parameters must be a JSON object")
        judgments = load_judgments(args.judgments)
        case_sets = load_case_sets(args.package)
    except (ValueError, json.JSONDecodeError, OSError) as exc:
        parser.error(str(exc))

    if args.adapter == "mock":
        if not args.allow_mock:
            parser.error("mock runs require --allow-mock")
        adapter = MockAdapter(args.mock_response)
        evidence_status = "mock-not-evidence"
    else:
        if not args.command:
            parser.error("command adapter requires --command")
        adapter = CommandAdapter(shlex.split(args.command))
        evidence_status = "unscored-model-output"

    selected = []
    allowed_types = set(args.case_type)
    for package_dir, case_set in case_sets:
        for case in case_set["cases"]:
            if allowed_types and case["type"] not in allowed_types:
                continue
            selected.append((package_dir, case_set, case))
    if args.max_cases:
        selected = selected[: args.max_cases]
    if not selected:
        parser.error("selection contains no cases")

    results = []
    for package_dir, case_set, case in selected:
        output = adapter.run(case_prompt(package_dir, case))
        judgment = judgments.get(case["id"])
        results.append({
            "slug": case_set["slug"],
            "package_version": case_set["package_version"],
            "case_id": case["id"],
            "case_type": case["type"],
            "given": case["given"],
            "rubric": {"expect": case["expect"], "reject": case["reject"]},
            "raw_output": output,
            "judgment": judgment,
        })

    judged = [item for item in results if item["judgment"]]
    report = {
        "schema_version": "1.0.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "model": args.model,
        "adapter": args.adapter,
        "parameters": parameters,
        "evidence_status": "human-scored" if judged and len(judged) == len(results) else evidence_status,
        "scoring_method": "declared judgments file" if judged else "unscored",
        "case_count": len(results),
        "case_set": sorted({f"{item['slug']}@{item['package_version']}" for item in results}),
        "results": results,
    }
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.stdout:
        sys.stdout.write(rendered)
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"wrote {len(results)} case result(s) to {args.output}")
    if args.adapter == "mock":
        print("mock output is harness-only and must not be cited as model evidence", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
