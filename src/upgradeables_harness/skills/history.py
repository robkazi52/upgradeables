"""Opt-in, local task-event history used only for Skill suggestions."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .common import HARNESS_DIR, SkillFactoryError, project_config


EVENT_FIELDS = (
    "event_id",
    "timestamp",
    "raw_task",
    "normalized_task",
    "task_archetype",
    "selected_recipe",
    "candidate_components",
    "environment_modifiers",
    "project_constraints",
    "requested_output_shape",
    "output_contract",
    "authority_mode",
    "component_composition",
    "required_inputs",
    "activation_boundary",
    "procedure_signature",
    "user_agent_overrides",
    "skill_used",
    "outcome",
)
PRIVATE_REASONING_KEYS = {
    "analysis",
    "chain-of-thought",
    "chain_of_thought",
    "hidden-reasoning",
    "hidden_reasoning",
    "private-reasoning",
    "private_reasoning",
    "reasoning-trace",
    "reasoning_trace",
}


def history_path(project_root: str | Path) -> Path:
    return Path(project_root).resolve() / HARNESS_DIR / "runtime" / "task-events.jsonl"


def history_enabled(project_root: str | Path) -> bool:
    config = project_config(Path(project_root).resolve())
    return config.get("record_task_events") is True


def _json_safe(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    if isinstance(value, dict):
        return {
            str(key): _json_safe(item)
            for key, item in value.items()
            if str(key).casefold() not in PRIVATE_REASONING_KEYS
        }
    return str(value)


def normalize_event(event: dict[str, Any]) -> dict[str, Any]:
    """Keep explicit task metadata while excluding private-reasoning fields."""

    if not isinstance(event, dict):
        raise SkillFactoryError("Task event must be an object.")
    clean = {
        key: _json_safe(event[key])
        for key in EVENT_FIELDS
        if key in event and event[key] is not None
    }
    timestamp = clean.get("timestamp")
    if not isinstance(timestamp, str) or not timestamp:
        timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        clean["timestamp"] = timestamp
    normalized = clean.get("normalized_task")
    raw = clean.get("raw_task")
    if not isinstance(normalized, str) or not normalized.strip():
        if isinstance(raw, str) and raw.strip():
            clean["normalized_task"] = " ".join(raw.casefold().split())
        else:
            raise SkillFactoryError("Task event requires normalized_task or raw_task.")
    if not clean.get("event_id"):
        identity = json.dumps(clean, sort_keys=True, ensure_ascii=False).encode("utf-8")
        clean["event_id"] = "evt-" + hashlib.sha256(identity).hexdigest()[:12]
    return {key: clean[key] for key in EVENT_FIELDS if key in clean}


def append_task_event(project_root: str | Path, event: dict[str, Any]) -> dict[str, Any]:
    """Append an event after the caller has established explicit opt-in."""

    clean = normalize_event(event)
    path = history_path(project_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(clean, ensure_ascii=False, sort_keys=False) + "\n")
    return clean


def record_task_event(
    project_root: str | Path,
    event: dict[str, Any],
    *,
    explicitly_requested: bool = False,
) -> dict[str, Any] | None:
    """Record only for `--record` or an explicit local config opt-in."""

    if not explicitly_requested and not history_enabled(project_root):
        return None
    return append_task_event(project_root, event)


def load_task_events(project_root: str | Path) -> list[dict[str, Any]]:
    path = history_path(project_root)
    if not path.is_file():
        return []
    events: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as error:
        raise SkillFactoryError(f"Cannot read task history {path}: {error}") from error
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise SkillFactoryError(
                f"Malformed task event at {path}:{number}: {error.msg}"
            ) from error
        if not isinstance(value, dict):
            raise SkillFactoryError(f"Task event at {path}:{number} is not an object.")
        events.append(value)
    return events
