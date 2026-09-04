"""Offline-first paired-condition experiment runner."""
from __future__ import annotations

import itertools
import json
import math
import random
import re
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from ...constants import HARNESS_VERSION, REGISTRY_VERSION
from ..budget import estimate_tokens
from ..compiler import COMPILER_VERSION, canonical_hash
from .conditions import build_condition
from .graders import grade
from .report import write_report
from .suites import load_suite

Adapter = Callable[[dict, dict, dict], str]
CORE_CONDITIONS = ("baseline", "static-full", "adaptive-runtime")


def mock_adapter(request: dict, task: dict, manifest: dict) -> str:
    """Deterministic expected-output adapter for plumbing tests, never evidence."""
    grader = task["grader"]
    if grader["type"] == "exact":
        return grader["expected"]
    if grader["type"] in {"contains-all", "contains-any"}:
        return " ".join(grader["values"])
    if grader["type"] == "json-fields":
        return json.dumps(grader["fields"], sort_keys=True)
    return ""


def validate_manifest(manifest: dict) -> None:
    required = {"experiment_id", "suite", "conditions", "model", "trials_per_task", "temperature", "seed_policy", "grader"}
    if not isinstance(manifest, dict):
        raise ValueError("Experiment manifest must be an object")
    missing = sorted(required - set(manifest))
    if missing:
        raise ValueError("Experiment manifest missing: " + ", ".join(missing))
    if manifest.get("schema_version", "1.0.0") != "1.0.0":
        raise ValueError("Unsupported experiment manifest schema_version")
    experiment_id = manifest["experiment_id"]
    if not isinstance(experiment_id, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", experiment_id):
        raise ValueError("experiment_id must be a filesystem-safe slug")
    if not isinstance(manifest["suite"], str) or not manifest["suite"].strip():
        raise ValueError("suite must be a non-empty string")
    conditions = manifest["conditions"]
    if not isinstance(conditions, list) or not conditions:
        raise ValueError("conditions must be a non-empty array")
    if not all(isinstance(condition, str) for condition in conditions):
        raise ValueError("conditions must contain only strings")
    if len(conditions) != len(set(conditions)):
        raise ValueError("conditions must not contain duplicates")
    unsupported = [condition for condition in conditions if condition not in CORE_CONDITIONS]
    if unsupported:
        raise ValueError("Unsupported core evaluation condition: " + ", ".join(unsupported))
    trials = manifest["trials_per_task"]
    if isinstance(trials, bool) or not isinstance(trials, int) or trials < 1:
        raise ValueError("trials_per_task must be a positive integer")
    temperature = manifest["temperature"]
    if isinstance(temperature, bool) or not isinstance(temperature, (int, float)) or not math.isfinite(temperature):
        raise ValueError("temperature must be a finite number")
    if not isinstance(manifest["model"], dict):
        raise ValueError("model must be an object")
    for field in ("adapter", "model"):
        if not isinstance(manifest["model"].get(field), str) or not manifest["model"][field].strip():
            raise ValueError(f"model.{field} must be a non-empty string")
    if not isinstance(manifest["seed_policy"], str) or not manifest["seed_policy"].strip():
        raise ValueError("seed_policy must be a non-empty string")
    if manifest["grader"] != "objective":
        raise ValueError("core evaluation runner supports only objective graders")
    order_seed = manifest.get("order_seed", 0)
    if isinstance(order_seed, bool) or not isinstance(order_seed, int):
        raise ValueError("order_seed must be an integer")


def condition_schedule(conditions: list[str], blocks: int, seed: int) -> list[tuple[str, ...]]:
    """Return deterministic, balanced condition orders for task/trial blocks."""
    permutations = list(itertools.permutations(conditions))
    random.Random(seed).shuffle(permutations)
    return [permutations[index % len(permutations)] for index in range(blocks)]


def _ungraded(kind: str | None, stage: str, error: Exception) -> dict:
    return {
        "schema_version": "1.0.0",
        "grader_kind": "deterministic",
        "grader_type": "objective",
        "grader": kind,
        "status": "ungraded",
        "success": None,
        "score": None,
        "details": {
            "error_stage": stage,
            "error_type": type(error).__name__,
            "error": str(error),
        },
    }


def run_experiment(manifest: dict, adapter: Adapter, output_root: str | Path) -> Path:
    validate_manifest(manifest)
    if not callable(adapter):
        raise ValueError("adapter must be callable")
    suite = load_suite(manifest["suite"])
    target = Path(output_root) / manifest["experiment_id"]
    target.mkdir(parents=True, exist_ok=False)
    complete_manifest = dict(manifest)
    complete_manifest.setdefault("schema_version", "1.0.0")
    complete_manifest["created_at"] = datetime.now(timezone.utc).isoformat()
    complete_manifest.setdefault("repository_commit", None)
    complete_manifest.setdefault("harness_version", HARNESS_VERSION)
    complete_manifest.setdefault("registry_version", REGISTRY_VERSION)
    complete_manifest.setdefault("runtime_compiler_version", COMPILER_VERSION)
    complete_manifest["suite_hash"] = canonical_hash(suite)
    complete_manifest["order_strategy"] = "balanced-permutations-v1"
    complete_manifest["scheduled_observations"] = (
        len(suite["tasks"]) * manifest["trials_per_task"] * len(manifest["conditions"])
    )
    complete_manifest["manifest_hash"] = canonical_hash({key: value for key, value in complete_manifest.items() if key != "manifest_hash"})
    (target / "manifest.json").write_text(json.dumps(complete_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")

    results = []
    seed = int(manifest.get("order_seed", 0))
    block_count = len(suite["tasks"]) * manifest["trials_per_task"]
    schedule = condition_schedule(manifest["conditions"], block_count, seed)
    with (target / "raw-results.jsonl").open("x", encoding="utf-8", newline="\n") as handle:
        schedule_index = 0
        for task in suite["tasks"]:
            for trial in range(manifest["trials_per_task"]):
                conditions = schedule[schedule_index]
                for order, condition in enumerate(conditions):
                    request = None
                    raw_response = None
                    observation_status = "completed"
                    try:
                        request = build_condition(
                            task["prompt"], condition,
                            model_profile=manifest.get("model_profile", "medium"),
                            max_directive_tokens=manifest.get("max_directive_tokens", 500),
                        )
                    except Exception as error:
                        observation_status = "condition-error"
                        graded = _ungraded(task.get("grader", {}).get("type"), "condition", error)
                    else:
                        try:
                            raw_response = adapter(request, task, deepcopy(complete_manifest))
                            if not isinstance(raw_response, str):
                                raise TypeError("evaluation adapter must return a string")
                        except Exception as error:
                            observation_status = "adapter-error"
                            graded = _ungraded(task.get("grader", {}).get("type"), "adapter", error)
                        else:
                            try:
                                graded = grade(raw_response, task["grader"])
                            except Exception as error:
                                observation_status = "grader-error"
                                graded = _ungraded(task.get("grader", {}).get("type"), "grader", error)
                    result = {
                        "schema_version": "1.0.0",
                        "experiment_id": complete_manifest["experiment_id"],
                        "manifest_hash": complete_manifest["manifest_hash"],
                        "recorded_at": datetime.now(timezone.utc).isoformat(),
                        "task_id": task["id"],
                        "task_family": task["family"],
                        "task_definition_hash": canonical_hash(task),
                        "trial_index": trial,
                        "schedule_index": schedule_index,
                        "condition_order": order,
                        "condition": condition,
                        "observation_status": observation_status,
                        "raw_request": request,
                        "request_hash": canonical_hash(request) if request is not None else None,
                        "condition_hash": request["condition_hash"] if request is not None else None,
                        "runtime_plan_hash": request["runtime_plan_hash"] if request is not None else None,
                        "compiled_instruction_hash": request["instruction_hash"] if request is not None else None,
                        "directive_token_estimate": estimate_tokens(request["instructions"]) if request is not None else 0,
                        "model": deepcopy(complete_manifest["model"]),
                        "generation_parameters": {"temperature": complete_manifest["temperature"]},
                        "seed_policy": complete_manifest["seed_policy"],
                        "raw_response": raw_response,
                        "raw_response_hash": canonical_hash(raw_response) if raw_response is not None else None,
                        "grade": graded,
                    }
                    results.append(result)
                    handle.write(json.dumps(result, ensure_ascii=False, sort_keys=True) + "\n")
                    handle.flush()
                schedule_index += 1
    write_report(target, complete_manifest, results)
    return target
