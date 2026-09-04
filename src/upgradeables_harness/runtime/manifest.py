"""Reproducible run artifacts with conservative secret redaction."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ..constants import HARNESS_VERSION, REGISTRY_VERSION
from .compiler import COMPILER_VERSION, canonical_hash

SECRET_PATTERNS = (
    re.compile(r"(?i)(authorization\s*:\s*bearer\s+)[^\s]+"),
    re.compile(r"(?i)((?:api[_-]?key|token|secret|password)\s*[=:]\s*)[^\s,;]+"),
    re.compile(r"\b(?:sk|gh[opusu])_[A-Za-z0-9_-]{12,}\b"),
)


def redact_secrets(value: str) -> str:
    output = value
    for pattern in SECRET_PATTERNS:
        output = pattern.sub(lambda match: (match.group(1) if match.lastindex else "") + "[REDACTED]", output)
    return output


def build_manifest(
    *,
    plan: dict,
    model_identifier: str,
    endpoint_type: str,
    generation_parameters: dict | None = None,
    trial_index: int = 0,
    repository_commit: str | None = None,
) -> dict:
    safe_parameters = json.loads(redact_secrets(json.dumps(generation_parameters or {})))
    manifest = {
        "schema_version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "repository_commit": repository_commit,
        "harness_version": HARNESS_VERSION,
        "registry_version": REGISTRY_VERSION,
        "runtime_compiler_version": COMPILER_VERSION,
        "task_resolution_hash": plan["task_resolution_hash"],
        "runtime_plan_hash": plan["manifest_hash"],
        "model_identifier": model_identifier,
        "endpoint_type": endpoint_type,
        "generation_parameters": safe_parameters,
        "trial_index": trial_index,
    }
    manifest["manifest_hash"] = canonical_hash(manifest)
    return manifest


def write_run_artifacts(
    directory: str | Path,
    *,
    manifest: dict,
    task: str,
    plan: dict,
    compiled_instructions: str,
    raw_response: str,
    metrics: dict,
) -> None:
    target = Path(directory)
    target.mkdir(parents=True, exist_ok=False)
    values = {
        "manifest.json": json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        "task.txt": redact_secrets(task) + "\n",
        "runtime-plan.json": json.dumps(plan, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        "compiled-instructions.txt": compiled_instructions + "\n",
        "raw-response.txt": raw_response,
        "metrics.json": json.dumps(metrics, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    }
    for name, content in values.items():
        (target / name).write_text(content, encoding="utf-8", newline="\n")
