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
from typing import Any, Callable

from ...constants import HARNESS_VERSION, REGISTRY_VERSION
from ..budget import estimate_tokens
from ..compiler import COMPILER_VERSION, canonical_hash
from .conditions import CANONICAL_CONDITIONS, CONDITION_ALIASES, build_condition, canonical_condition
from .graders import grade
from .report import write_report
from .suites import fixed_resolution_inventory, load_suite

Adapter = Callable[[dict, dict, dict], str | dict]
CORE_CONDITIONS = (*CANONICAL_CONDITIONS, *CONDITION_ALIASES)
SECRET_KEY_NAMES = {
    "apikey", "token", "secret", "password", "authorization",
    "accesstoken", "authtoken", "bearertoken", "refreshtoken",
    "clientsecret", "secretkey", "authorizationheader",
}
SECRET_KEY_SUFFIXES = (
    "apikey", "accesstoken", "authtoken", "bearertoken", "refreshtoken",
    "clientsecret", "secretkey", "password",
)


def _validate_json_value(value: Any, path: str) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError(f"{path} keys must be strings")
            _validate_json_value(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _validate_json_value(item, f"{path}[{index}]")
    elif isinstance(value, float) and not math.isfinite(value):
        raise ValueError(f"{path} must not contain NaN or infinity")
    elif value is not None and not isinstance(value, (str, int, float, bool)):
        raise ValueError(f"{path} must contain only JSON-compatible values")


def _reject_secret_keys(value: Any, path: str = "manifest") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError(f"{path} keys must be strings")
            normalized = re.sub(r"[^a-z0-9]", "", key.casefold())
            if normalized in SECRET_KEY_NAMES or normalized.endswith(SECRET_KEY_SUFFIXES):
                raise ValueError(f"Experiment manifest must not contain secret-bearing key: {path}.{key}")
            _reject_secret_keys(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _reject_secret_keys(item, f"{path}[{index}]")


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
    _validate_json_value(manifest, "manifest")
    _reject_secret_keys(manifest)
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
    canonical = [canonical_condition(condition) for condition in conditions]
    if len(canonical) != len(set(canonical)):
        raise ValueError("conditions must not contain aliases for the same evaluation mode")
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
    top_endpoint = manifest.get("endpoint_origin")
    model_endpoint = manifest["model"].get("endpoint_origin")
    if top_endpoint is not None and model_endpoint is not None and top_endpoint != model_endpoint:
        raise ValueError("endpoint_origin must match model.endpoint_origin")
    endpoint = top_endpoint if top_endpoint is not None else model_endpoint
    if endpoint is not None:
        if not isinstance(endpoint, str):
            raise ValueError("endpoint_origin must be a string or null")
        adapter_name = manifest["model"]["adapter"]
        if adapter_name in {"ollama", "openai-compatible"}:
            from .live import validate_endpoint_origin
            if validate_endpoint_origin(endpoint, adapter_name) != endpoint:
                raise ValueError("endpoint_origin must be a normalized credential-free origin")
        elif any(value in endpoint for value in ("@", "?", "#")):
            raise ValueError("endpoint_origin must not contain credentials, query, or fragment")
    if not isinstance(manifest["seed_policy"], str) or not manifest["seed_policy"].strip():
        raise ValueError("seed_policy must be a non-empty string")
    if manifest["grader"] != "objective":
        raise ValueError("core evaluation runner supports only objective graders")
    order_seed = manifest.get("order_seed", 0)
    if isinstance(order_seed, bool) or not isinstance(order_seed, int):
        raise ValueError("order_seed must be an integer")
    generation_parameters = manifest.get("generation_parameters", {})
    if not isinstance(generation_parameters, dict):
        raise ValueError("generation_parameters must be an object")
    if "temperature" in generation_parameters and generation_parameters["temperature"] != temperature:
        raise ValueError("generation_parameters.temperature must match temperature")
    if manifest["model"]["adapter"] in {"ollama", "openai-compatible"}:
        reserved_generation = sorted(set(generation_parameters) & {"model", "messages"})
        if reserved_generation:
            raise ValueError(
                "live evaluation generation_parameters cannot replace: "
                + ", ".join(reserved_generation)
            )
        if generation_parameters.get("stream", False) is not False:
            raise ValueError("live evaluation requires generation_parameters.stream=false")


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


def _manifest_contract_hash(manifest: dict) -> str:
    """Hash immutable run configuration while excluding the live completion counter."""
    return canonical_hash({
        key: value
        for key, value in manifest.items()
        if key not in {"manifest_hash", "request_count_completed"}
    })


def _adapter_error(value: Any) -> RuntimeError:
    if isinstance(value, dict):
        message = value.get("message") or value.get("kind") or json.dumps(value, sort_keys=True)
    else:
        message = str(value)
    return RuntimeError(message)


def _normalize_adapter_result(value: str | dict) -> dict:
    """Normalize legacy text and structured live-adapter results without losing evidence."""
    if isinstance(value, str):
        return {
            "response_text": value,
            "provider_request": None,
            "provider_raw_response": None,
            "usage": None,
            "latency_ms": None,
            "model_id": None,
            "provider_timing": None,
            "finish_reason": None,
            "partial": None,
            "truncated": None,
            "error": None,
        }
    if not isinstance(value, dict):
        raise TypeError("evaluation adapter must return a string or result object")
    _validate_json_value(value, "evaluation adapter result")
    text = value.get("response_text")
    if not isinstance(text, str):
        raise TypeError("evaluation adapter result.response_text must be a string")
    usage = value.get("usage")
    if usage is not None and not isinstance(usage, dict):
        raise TypeError("evaluation adapter result.usage must be an object or null")
    latency = value.get("latency_ms")
    if latency is not None and (
        isinstance(latency, bool)
        or not isinstance(latency, (int, float))
        or not math.isfinite(latency)
        or latency < 0
    ):
        raise TypeError("evaluation adapter result.latency_ms must be a non-negative finite number or null")
    error = value.get("error")
    if error is not None and not isinstance(error, dict):
        raise TypeError("evaluation adapter result.error must be an object or null")
    for field in ("model_id", "finish_reason"):
        if value.get(field) is not None and not isinstance(value[field], str):
            raise TypeError(f"evaluation adapter result.{field} must be a string or null")
    timing = value.get("provider_timing")
    if timing is not None and not isinstance(timing, dict):
        raise TypeError("evaluation adapter result.provider_timing must be an object or null")
    for field in ("partial", "truncated"):
        if value.get(field) is not None and not isinstance(value[field], bool):
            raise TypeError(f"evaluation adapter result.{field} must be a boolean or null")
    return {
        "response_text": text,
        "provider_request": deepcopy(value.get("provider_request")),
        "provider_raw_response": deepcopy(value.get("raw_response")),
        "usage": deepcopy(usage),
        "latency_ms": latency,
        "model_id": value.get("model_id"),
        "provider_timing": deepcopy(value.get("provider_timing")),
        "finish_reason": value.get("finish_reason"),
        "partial": value.get("partial"),
        "truncated": value.get("truncated"),
        "error": deepcopy(error),
    }


def prepare_experiment(manifest: dict) -> dict:
    """Validate and expand a deterministic experiment plan without writes or I/O."""
    validate_manifest(manifest)
    suite = load_suite(manifest["suite"])
    requested_conditions = list(manifest["conditions"])
    conditions = [canonical_condition(condition) for condition in requested_conditions]
    fixed_resolutions, fixed_hashes = fixed_resolution_inventory(suite)
    if "adaptive-fixed-resolution" in conditions:
        missing = [task["id"] for task in suite["tasks"] if task["id"] not in fixed_resolutions]
        if missing:
            raise ValueError(
                "adaptive-fixed-resolution requires a fixed TaskResolution for every task; missing: "
                + ", ".join(missing)
            )
    prepared = deepcopy(manifest)
    prepared.setdefault("schema_version", "1.0.0")
    prepared["requested_conditions"] = requested_conditions
    prepared["conditions"] = conditions
    prepared.setdefault("repository_commit", None)
    prepared.setdefault("harness_version", HARNESS_VERSION)
    prepared.setdefault("registry_version", REGISTRY_VERSION)
    prepared.setdefault("runtime_compiler_version", COMPILER_VERSION)
    prepared["suite_hash"] = canonical_hash(suite)
    prepared["order_strategy"] = "balanced-permutations-v1"
    planned = len(suite["tasks"]) * manifest["trials_per_task"] * len(conditions)
    prepared["scheduled_observations"] = planned
    prepared["evaluation_modes"] = conditions
    prepared["adapter"] = prepared["model"]["adapter"]
    prepared["model_id"] = prepared["model"]["model"]
    prepared.setdefault(
        "endpoint_type",
        prepared["model"].get("endpoint_type", "none" if prepared["adapter"] == "mock" else "unknown"),
    )
    prepared.setdefault("endpoint_origin", prepared["model"].get("endpoint_origin"))
    prepared["fixed_resolution_policy"] = (
        "required-per-task-v1"
        if "adaptive-fixed-resolution" in conditions
        else ("available-not-requested-v1" if fixed_resolutions else "none")
    )
    prepared["fixed_resolutions"] = fixed_resolutions
    prepared["fixed_resolution_hashes"] = fixed_hashes
    prepared["request_count_planned"] = planned
    prepared["request_count_completed"] = 0
    generation_parameters = deepcopy(prepared.get("generation_parameters", {}))
    generation_parameters.setdefault("temperature", prepared["temperature"])
    prepared["generation_parameters"] = generation_parameters
    prepared["trial_count"] = prepared["trials_per_task"]
    prepared["condition_order_seed"] = int(prepared.get("order_seed", 0))
    block_count = len(suite["tasks"]) * manifest["trials_per_task"]
    schedule = condition_schedule(conditions, block_count, prepared["condition_order_seed"])
    prepared["condition_schedule_hash"] = canonical_hash([list(order) for order in schedule])
    prepared["configuration_hash"] = canonical_hash({
        key: value
        for key, value in prepared.items()
        if key not in {"configuration_hash", "manifest_hash", "request_count_completed"}
    })
    return {
        "manifest": prepared,
        "suite": suite,
        "schedule": [list(order) for order in schedule],
        "task_ids": [task["id"] for task in suite["tasks"]],
        "fixed_resolution_availability": {
            "available": len(fixed_resolutions),
            "required": len(suite["tasks"]) if "adaptive-fixed-resolution" in conditions else 0,
            "missing": [task["id"] for task in suite["tasks"] if task["id"] not in fixed_resolutions],
        },
    }


def run_experiment(manifest: dict, adapter: Adapter, output_root: str | Path) -> Path:
    if not callable(adapter):
        raise ValueError("adapter must be callable")
    preflight = prepare_experiment(manifest)
    suite = preflight["suite"]
    schedule = [tuple(order) for order in preflight["schedule"]]
    complete_manifest = preflight["manifest"]
    target = Path(output_root) / manifest["experiment_id"]
    target.mkdir(parents=True, exist_ok=False)
    complete_manifest["created_at"] = datetime.now(timezone.utc).isoformat()
    complete_manifest["manifest_hash_scope"] = (
        "immutable run contract; excludes manifest_hash and request_count_completed"
    )
    complete_manifest["manifest_hash"] = _manifest_contract_hash(complete_manifest)
    (target / "manifest.json").write_text(json.dumps(complete_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")

    results = []
    request_count_completed = 0
    with (target / "raw-results.jsonl").open("x", encoding="utf-8", newline="\n") as handle:
        schedule_index = 0
        for task in suite["tasks"]:
            for trial in range(manifest["trials_per_task"]):
                scheduled_conditions = schedule[schedule_index]
                for order, condition in enumerate(scheduled_conditions):
                    request = None
                    adapter_invoked = False
                    raw_response = None
                    provider_request = None
                    provider_raw_response = None
                    usage = None
                    latency_ms = None
                    response_model_id = None
                    provider_timing = None
                    finish_reason = None
                    partial = None
                    truncated = None
                    observation_error = None
                    observation_status = "completed"
                    try:
                        request = build_condition(
                            task["prompt"], condition,
                            fixed_resolution=task.get("fixed_resolution"),
                            model_profile=manifest.get("model_profile", "medium"),
                            max_directive_tokens=manifest.get("max_directive_tokens", 500),
                        )
                    except Exception as error:
                        observation_status = "condition-error"
                        observation_error = {
                            "stage": "condition", "type": type(error).__name__, "message": str(error),
                        }
                        graded = _ungraded(task.get("grader", {}).get("type"), "condition", error)
                    else:
                        try:
                            adapter_invoked = True
                            adapter_value = adapter(request, task, deepcopy(complete_manifest))
                            adapter_result = _normalize_adapter_result(adapter_value)
                        except Exception as error:
                            observation_status = "adapter-error"
                            observation_error = {
                                "stage": "adapter", "type": type(error).__name__, "message": str(error),
                            }
                            graded = _ungraded(task.get("grader", {}).get("type"), "adapter", error)
                        else:
                            raw_response = adapter_result["response_text"]
                            provider_request = adapter_result["provider_request"]
                            provider_raw_response = adapter_result["provider_raw_response"]
                            usage = adapter_result["usage"]
                            latency_ms = adapter_result["latency_ms"]
                            response_model_id = adapter_result["model_id"]
                            provider_timing = adapter_result["provider_timing"]
                            finish_reason = adapter_result["finish_reason"]
                            partial = adapter_result["partial"]
                            truncated = adapter_result["truncated"]
                            if adapter_result["error"] is not None:
                                observation_status = "adapter-error"
                                observation_error = {
                                    "stage": "adapter",
                                    "type": "AdapterResponseError",
                                    "message": str(
                                        adapter_result["error"].get("message")
                                        or adapter_result["error"].get("kind")
                                        or "adapter returned an error"
                                    ),
                                    "details": adapter_result["error"],
                                }
                                graded = _ungraded(
                                    task.get("grader", {}).get("type"),
                                    "adapter",
                                    _adapter_error(adapter_result["error"]),
                                )
                            else:
                                try:
                                    graded = grade(raw_response, task["grader"])
                                except Exception as error:
                                    observation_status = "grader-error"
                                    observation_error = {
                                        "stage": "grader", "type": type(error).__name__, "message": str(error),
                                    }
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
                        "condition": request["condition"] if request is not None else canonical_condition(condition),
                        "evaluation_mode": request.get("evaluation_mode", canonical_condition(condition)) if request is not None else canonical_condition(condition),
                        "observation_status": observation_status,
                        "error": observation_error,
                        "raw_request": request,
                        "request_hash": canonical_hash(request) if request is not None else None,
                        "condition_hash": request["condition_hash"] if request is not None else None,
                        "runtime_plan_hash": request["runtime_plan_hash"] if request is not None else None,
                        "task_resolution_source": request.get("task_resolution_source") if request is not None else None,
                        "task_resolution_hash": request.get("task_resolution_hash") if request is not None else None,
                        "fixed_resolution_hash": request.get("fixed_resolution_hash") if request is not None else None,
                        "compiled_instruction_hash": request["instruction_hash"] if request is not None else None,
                        "directive_token_estimate": estimate_tokens(request["instructions"]) if request is not None else 0,
                        "model": deepcopy(complete_manifest["model"]),
                        "generation_parameters": deepcopy(complete_manifest["generation_parameters"]),
                        "seed_policy": complete_manifest["seed_policy"],
                        "raw_response": raw_response,
                        "raw_response_hash": canonical_hash(raw_response) if raw_response is not None else None,
                        "provider_request": provider_request,
                        "provider_request_hash": canonical_hash(provider_request) if provider_request is not None else None,
                        "provider_raw_response": provider_raw_response,
                        "usage": usage,
                        "latency_ms": latency_ms,
                        "response_model_id": response_model_id,
                        "provider_timing": provider_timing,
                        "finish_reason": finish_reason,
                        "partial": partial,
                        "truncated": truncated,
                        "grade": graded,
                    }
                    results.append(result)
                    handle.write(json.dumps(result, ensure_ascii=False, sort_keys=True) + "\n")
                    handle.flush()
                    if adapter_invoked:
                        request_count_completed += 1
                        complete_manifest["request_count_completed"] = request_count_completed
                        (target / "manifest.json").write_text(
                            json.dumps(complete_manifest, indent=2, sort_keys=True) + "\n",
                            encoding="utf-8",
                            newline="\n",
                        )
                schedule_index += 1
    complete_manifest["request_count_completed"] = request_count_completed
    (target / "manifest.json").write_text(
        json.dumps(complete_manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_report(target, complete_manifest, results)
    return target
