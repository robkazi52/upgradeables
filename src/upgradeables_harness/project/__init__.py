"""Deterministic, shallow project inspection and profile selection."""

from .inspect import inspect_project
from .profile import recommend_project
from .root import find_project_root

__all__ = ["find_project_root", "inspect_project", "recommend_project"]
