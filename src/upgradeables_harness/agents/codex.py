"""Codex adapter fragment."""
from .generic import fragment as generic_fragment


def fragment() -> str:
    return generic_fragment() + """

When shell access is available, you may run `upgradeables task "<task>" --json`. Otherwise use the project-local files directly. Treat `AGENTS.md` scope and current user authority as controlling."""
