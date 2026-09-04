"""Public v0.4 runtime compiler API."""
from __future__ import annotations

from pathlib import Path

from ..resolver.task import resolve_task
from .compiler import COMPILER_VERSION, RuntimeCompileError, compile
from .models import HostCapabilities, RuntimeCompileRequest, RuntimeContext


def compile_request(request: RuntimeCompileRequest | dict) -> dict:
    value = RuntimeCompileRequest.from_value(request)
    return compile(value.task_resolution, value.context())


def compile_task(
    task: str,
    *,
    project: str | Path | dict | None = None,
    model_profile: str = "medium",
    max_directive_tokens: int = 500,
    host: HostCapabilities | dict | None = None,
    use_project_profile: bool = True,
) -> dict:
    resolution = resolve_task(task, project=project, use_project_profile=use_project_profile)
    context = RuntimeContext(
        model_profile=model_profile,
        max_directive_tokens=max_directive_tokens,
        host=HostCapabilities.from_value(host),
    )
    return compile(resolution, context)


__all__ = [
    "COMPILER_VERSION", "HostCapabilities", "RuntimeCompileError", "RuntimeCompileRequest",
    "RuntimeContext", "compile", "compile_request", "compile_task",
]
