"""Claude Code adapter fragment."""
from .generic import fragment as generic_fragment


def fragment() -> str:
    return generic_fragment() + """

Use only tools and project context actually available in this session. This fragment does not grant persistent memory, external access, or mutation authority."""
