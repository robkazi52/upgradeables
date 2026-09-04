#!/usr/bin/env python3
"""Build the deterministic v0.4 Python-debugging example."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from upgradeables_harness.resolver.task import resolve_task
from upgradeables_harness.runtime import compile
from upgradeables_harness.runtime.adapters.openai_compatible import build_chat_completions_request

TARGET = ROOT / "examples" / "runtime" / "python-debugging"
TASK = "Fix the failing parser test without refactoring unrelated code."


def _json(value) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def outputs() -> dict[str, str]:
    resolution = resolve_task(TASK)
    plan = compile(resolution, {"model_profile": "medium", "max_directive_tokens": 500})
    baseline = {"model": "example-model", "messages": [{"role": "user", "content": TASK}]}
    adaptive = build_chat_completions_request(
        model="example-model", user_content=TASK, plan=plan,
        base_instructions="You are a software-maintenance assistant.",
    )
    mock = {
        "evidence_status": "mock-non-evidence",
        "note": "Illustrative shape only; no model or adapter was executed.",
        "response": "Located the parser boundary defect, applied a local correction, and verified the affected test and neighboring parser tests.",
    }
    return {
        "task.txt": TASK + "\n",
        "task-resolution.json": _json(resolution),
        "runtime-plan.json": _json(plan),
        "compiled-instructions.txt": plan["instruction_capsule"] + "\n",
        "baseline-request.json": _json(baseline),
        "adaptive-request.json": _json(adaptive),
        "mock-result.json": _json(mock),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    generated = outputs()
    if args.check:
        stale = [name for name, text in generated.items() if not (TARGET / name).is_file() or (TARGET / name).read_text(encoding="utf-8") != text]
        if stale:
            print("runtime example is stale: " + ", ".join(stale), file=sys.stderr)
            return 1
        print("runtime example build: OK")
        return 0
    TARGET.mkdir(parents=True, exist_ok=True)
    for name, text in generated.items():
        (TARGET / name).write_text(text, encoding="utf-8", newline="\n")
    print("runtime example built")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
