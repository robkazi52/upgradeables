"""Conservative host-capability declarations."""
from __future__ import annotations

from pathlib import Path


def detect_host_capabilities(project_root: Path) -> dict[str, str]:
    """Report only project-file persistence; do not infer agent/model powers."""
    writable_parent = project_root.exists() and project_root.is_dir()
    return {
        "shell": "unknown",
        "web": "unknown",
        "durable_state": "project-files" if writable_parent else "unknown",
        "parallel_agents": "unknown",
    }
