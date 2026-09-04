"""Load bundled or source-checkout runtime evaluation suites."""
from __future__ import annotations

from copy import deepcopy

from ...registry.query import normalize
from ..compiler import RuntimeCompileError, canonical_hash, validate_task_resolution
from ..data import load_runtime_registry, runtime_components


def list_suites() -> list[dict]:
    result = []
    suites = load_runtime_registry().get("eval_suites", [])
    if not isinstance(suites, list):
        raise ValueError("Invalid runtime registry: eval_suites must be an array")
    for data in suites:
        _validate_suite(data, expected_slug=data.get("slug") if isinstance(data, dict) else "<unknown>")
        result.append({key: data[key] for key in ("slug", "description", "license")})
    return result


def load_suite(slug: str) -> dict:
    suites = load_runtime_registry().get("eval_suites", [])
    if not isinstance(suites, list):
        raise ValueError("Invalid runtime registry: eval_suites must be an array")
    data = next((item for item in suites if isinstance(item, dict) and item.get("slug") == slug), None)
    if data is None:
        raise ValueError(f"Unknown evaluation suite: {slug}")
    _validate_suite(data, expected_slug=slug)
    return deepcopy(data)


def fixed_resolution_inventory(suite: dict) -> tuple[dict[str, dict], dict[str, str]]:
    """Return copied fixed resolutions and their canonical hashes by task ID."""
    resolutions = {}
    hashes = {}
    for task in suite["tasks"]:
        resolution = task.get("fixed_resolution")
        if resolution is not None:
            resolutions[task["id"]] = deepcopy(resolution)
            hashes[task["id"]] = canonical_hash(resolution)
    return resolutions, hashes


def _validate_suite(data: object, *, expected_slug: str) -> None:
    if not isinstance(data, dict):
        raise ValueError(f"Invalid evaluation suite: {expected_slug}")
    if data.get("schema_version") != "1.0.0" or data.get("slug") != expected_slug:
        raise ValueError(f"Invalid evaluation suite: {expected_slug}")
    for field in ("description", "license"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            raise ValueError(f"Invalid evaluation suite {expected_slug}: {field} must be non-empty")
    tasks = data.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        raise ValueError(f"Invalid evaluation suite {expected_slug}: tasks must be non-empty")
    seen = set()
    for task in tasks:
        if not isinstance(task, dict):
            raise ValueError(f"Invalid evaluation suite {expected_slug}: each task must be an object")
        for field in ("id", "family", "prompt"):
            if not isinstance(task.get(field), str) or not task[field].strip():
                raise ValueError(f"Invalid evaluation suite {expected_slug}: task {field} must be non-empty")
        if task["id"] in seen:
            raise ValueError(f"Invalid evaluation suite {expected_slug}: duplicate task id {task['id']}")
        seen.add(task["id"])
        grader = task.get("grader")
        if not isinstance(grader, dict) or not isinstance(grader.get("type"), str):
            raise ValueError(f"Invalid evaluation suite {expected_slug}: task {task['id']} has no grader")
        if "fixed_resolution" in task:
            resolution = task["fixed_resolution"]
            if not isinstance(resolution, dict):
                raise ValueError(
                    f"Invalid evaluation suite {expected_slug}: task {task['id']} fixed_resolution must be an object"
                )
            if resolution.get("query") != task["prompt"]:
                raise ValueError(
                    f"Invalid evaluation suite {expected_slug}: task {task['id']} fixed_resolution query must match prompt"
                )
            if resolution.get("normalized_task") != normalize(task["prompt"]):
                raise ValueError(
                    f"Invalid evaluation suite {expected_slug}: task {task['id']} fixed_resolution normalized_task is stale"
                )
            try:
                validate_task_resolution(resolution, runtime_components())
            except RuntimeCompileError as error:
                raise ValueError(
                    f"Invalid evaluation suite {expected_slug}: task {task['id']} fixed_resolution: {error}"
                ) from error
