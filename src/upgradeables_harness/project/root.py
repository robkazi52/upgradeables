"""Project-root resolution without executing or importing target code."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

PROJECT_MANIFESTS = (
    "pyproject.toml", "requirements.txt", "setup.py", "package.json",
    "tsconfig.json", "Cargo.toml", "go.mod", "pom.xml", "build.gradle",
)


@dataclass(frozen=True)
class RootResolution:
    root: Path
    source: str


def _directory(value: str | Path | None) -> Path:
    path = Path.cwd() if value is None else Path(value).expanduser()
    path = path.resolve()
    if not path.exists():
        raise FileNotFoundError(f"project path does not exist: {path}")
    return path.parent if path.is_file() else path


def _ancestors(start: Path):
    yield start
    yield from start.parents


def resolve_project_root(
    explicit: str | Path | None = None,
    *,
    start: str | Path | None = None,
) -> RootResolution:
    """Resolve explicit path, then nearest harness, Git root, manifest, or cwd."""
    if explicit is not None:
        return RootResolution(_directory(explicit), "explicit")
    origin = _directory(start)
    for candidate in _ancestors(origin):
        if (candidate / ".upgradeables").is_dir():
            return RootResolution(candidate, "nearest-harness")
    for candidate in _ancestors(origin):
        if (candidate / ".git").exists():
            return RootResolution(candidate, "nearest-git")
    for candidate in _ancestors(origin):
        if any((candidate / marker).is_file() for marker in PROJECT_MANIFESTS):
            return RootResolution(candidate, "nearest-manifest")
    return RootResolution(origin, "current-directory")


def find_project_root(start: str | Path | None = None) -> Path:
    """Return the selected root for a path or the current directory."""
    return resolve_project_root(start=start).root
