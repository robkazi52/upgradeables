"""GitHub Copilot adapter fragment."""
from .generic import fragment as generic_fragment


def fragment() -> str:
    return generic_fragment() + """

Keep suggestions grounded in the current repository and the small project-local harness files; do not copy the complete Upgradeables registry into context."""
