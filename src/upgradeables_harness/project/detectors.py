"""Shallow filesystem-signal detectors. File contents are never executed."""
from __future__ import annotations

from pathlib import Path

FILE_SIGNALS = {
    "pyproject.toml": ("Python project marker", "python"),
    "requirements.txt": ("Python dependency marker", "python"),
    "setup.py": ("Python packaging marker", "python"),
    "package.json": ("JavaScript package marker", "javascript"),
    "tsconfig.json": ("TypeScript configuration marker", "typescript"),
    "Cargo.toml": ("Rust package marker", "rust"),
    "go.mod": ("Go module marker", "go"),
    "pom.xml": ("Java Maven marker", "java"),
    "build.gradle": ("Java/Gradle marker", "java"),
    "Dockerfile": ("Container build marker", None),
    "mkdocs.yml": ("Documentation build marker", None),
    "conf.py": ("Sphinx documentation marker", "python"),
    "AGENTS.md": ("Agent instructions marker", None),
    "CLAUDE.md": ("Claude instructions marker", None),
    ".github/copilot-instructions.md": ("Copilot instructions marker", None),
}
DIRECTORY_SIGNALS = {
    ".git": "Git repository marker",
    ".github/workflows": "CI workflow marker",
    "tests": "Test directory marker",
    "test": "Test directory marker",
    "docs": "Documentation directory marker",
    "notebooks": "Notebook directory marker",
    "papers": "Research corpus marker",
    "sources": "Source corpus marker",
    "references": "Reference corpus marker",
    "spec": "Specification directory marker",
    "specs": "Specification directory marker",
    "architecture": "Architecture reference marker",
}


def detect_project_signals(root: Path) -> dict:
    signals: list[dict[str, str]] = []
    languages: set[str] = set()
    for relative, (reason, language) in FILE_SIGNALS.items():
        if (root / relative).is_file():
            signals.append({"type": "file", "value": relative, "reason": reason})
            if language:
                languages.add(language)
    for relative, reason in DIRECTORY_SIGNALS.items():
        if (root / relative).is_dir():
            signals.append({"type": "directory", "value": relative, "reason": reason})
    try:
        suffixes = {path.suffix.lower() for path in root.iterdir() if path.is_file()}
        for suffix, reason in (
            (".ipynb", "Notebook marker"),
            (".bib", "Bibliography marker"),
            (".csv", "Tabular-data marker"),
            (".parquet", "Tabular-data marker"),
        ):
            if suffix in suffixes:
                signals.append({"type": "file-pattern", "value": f"*{suffix}", "reason": reason})
    except OSError:
        pass
    values = {item["value"] for item in signals}
    git = ".git" in values
    tests = bool(values & {"tests", "test"})
    documentation = "docs" in values
    ci = ".github/workflows" in values
    research = bool(values & {"papers", "sources", "references", "*.ipynb", "*.bib"})
    agent_project = bool(values & {"AGENTS.md", "CLAUDE.md", ".github/copilot-instructions.md"})
    project_types: list[str] = []
    if languages:
        project_types.append("software-development")
    if research:
        project_types.append("research")
    if documentation:
        project_types.append("documentation")
    if values & {"*.ipynb", "*.csv", "*.parquet"}:
        project_types.append("data-analysis")
    if agent_project:
        project_types.append("agent-development")
    if not project_types:
        project_types.append("general")
    reference_roots = [
        f"{name}/" for name in ("docs", "spec", "specs", "architecture", "papers", "sources", "references")
        if (root / name).is_dir()
    ]
    return {
        "languages": sorted(languages),
        "frameworks": [],
        "project_types": project_types,
        "features": {
            "git": git,
            "tests": tests,
            "documentation": documentation,
            "ci": ci,
            "pull_requests": git and ci,
            "long_context": research or len(reference_roots) >= 3,
        },
        "signals": sorted(signals, key=lambda item: (item["type"], item["value"])),
        "reference_roots": reference_roots,
    }
