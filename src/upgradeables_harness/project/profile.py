"""Weak project-profile priors and project-level recommendations."""
from __future__ import annotations

import json
from argparse import Namespace
from pathlib import Path

from ..registry.load import load_profiles
from .inspect import inspect_project

PROFILE_VERSION = "1.0.0"
PROFILE_ORDER = (
    "general", "software-development", "research", "long-context", "authoring",
    "data-analysis", "medical-evidence", "legal-evidence", "agent-development",
    "documentation",
)
PROFILES = {
    "general": {
        "likely_recipes": ["decision-support", "education-explanation"],
        "candidate_cross_cutting": ["task-set-lock-in", "bounded-exit"],
        "likely_exclusions": ["meta-supervisor", "multiverse-reasoning"],
    },
    "software-development": {
        "likely_recipes": ["coding-debugging", "code-review", "architecture-skill-building"],
        "candidate_cross_cutting": ["task-set-lock-in", "micro-repair", "invariance-stress-scaffold", "anti-tunnel-vision", "bidirectional-consistency"],
        "likely_exclusions": ["multi-truth-gating"],
    },
    "research": {
        "likely_recipes": ["research-skill", "source-grounded-analysis"],
        "candidate_cross_cutting": ["grounding-no-invention", "citation-fidelity", "epistemic-status-gating", "scoped-loader"],
        "likely_exclusions": ["external-state-automation"],
    },
    "long-context": {
        "likely_recipes": ["long-context-corpus", "long-context-source-fidelity"],
        "candidate_cross_cutting": ["activation-budget-funnel", "scoped-loader", "stable-long-context", "working-memory-lock-in"],
        "likely_exclusions": ["meta-supervisor"],
    },
    "authoring": {
        "likely_recipes": ["authoring", "creative-ideation"],
        "candidate_cross_cutting": ["style-alignment", "structured-refinement", "grounding-no-invention"],
        "likely_exclusions": ["external-state-automation"],
    },
    "data-analysis": {
        "likely_recipes": ["decision-support", "source-grounded-analysis"],
        "candidate_cross_cutting": ["critical-atomic-verification", "bidirectional-consistency", "epistemic-status-gating"],
        "likely_exclusions": ["multiverse-reasoning"],
    },
    "medical-evidence": {
        "likely_recipes": ["medical-evidence", "source-grounded-analysis", "high-stakes-reasoning"],
        "candidate_cross_cutting": ["grounding-no-invention", "citation-fidelity", "risk-tier-scaling", "fail-closed-abstention"],
        "likely_exclusions": ["power-mode"],
    },
    "legal-evidence": {
        "likely_recipes": ["legal-evidence", "source-grounded-analysis", "high-stakes-reasoning"],
        "candidate_cross_cutting": ["grounding-no-invention", "citation-fidelity", "truth-priority-hierarchy", "fail-closed-abstention"],
        "likely_exclusions": ["power-mode"],
    },
    "agent-development": {
        "likely_recipes": ["architecture-skill-building", "multi-agent-orchestration", "deterministic-intake-routing"],
        "candidate_cross_cutting": ["task-set-lock-in", "architect-orchestrator", "state-routing-bus", "specificity-penalty-gate"],
        "likely_exclusions": ["external-state-automation"],
    },
    "documentation": {
        "likely_recipes": ["authoring", "education-explanation", "long-context-source-fidelity"],
        "candidate_cross_cutting": ["pedagogical-alignment", "style-alignment", "grounding-no-invention", "placeholder-suppression"],
        "likely_exclusions": ["multiverse-reasoning"],
    },
}

# The bundled snapshot is the installed runtime authority. The literal table above
# remains a source-tree fallback for partial developer checkouts.
try:
    _bundled_profiles = load_profiles().get("profiles", [])
except (OSError, ValueError, KeyError):
    _bundled_profiles = []
if _bundled_profiles:
    PROFILES = {
        item["slug"]: {
            "likely_recipes": item["likely_recipes"],
            "candidate_cross_cutting": item["candidate_cross_cutting"],
            "likely_exclusions": item["likely_exclusions"],
        }
        for item in _bundled_profiles
    }


def select_profiles(inspection: dict, preferred: list[str] | None = None) -> list[str]:
    selected = []
    for slug in preferred or []:
        if slug not in PROFILES:
            raise ValueError(f"unknown project profile: {slug}")
        if slug not in selected:
            selected.append(slug)
    if selected:
        return selected
    for slug in inspection.get("project_types", []):
        if slug in PROFILES and slug not in selected:
            selected.append(slug)
    if inspection.get("features", {}).get("long_context") and "long-context" not in selected:
        selected.append("long-context")
    return selected or ["general"]


def _unique(values):
    return list(dict.fromkeys(values))


def recommend_project(
    project: str | Path | None = None,
    *,
    preferred_profiles: list[str] | None = None,
    inspection: dict | None = None,
) -> dict:
    inspected = inspection or inspect_project(project)
    profiles = select_profiles(inspected, preferred_profiles)
    recipes = _unique(value for slug in profiles for value in PROFILES[slug]["likely_recipes"])
    components = _unique(
        value for slug in profiles for value in PROFILES[slug]["candidate_cross_cutting"]
    )
    exclusions = _unique(value for slug in profiles for value in PROFILES[slug]["likely_exclusions"])
    reasons = {
        slug: [f"{profile} project profile" for profile in profiles if slug in PROFILES[profile]["likely_recipes"]]
        for slug in recipes
    }
    return {
        "schema_version": "1.0.0",
        "registry_version": "0.2.1",
        "selection_only": True,
        "project_root": inspected["selected_root"],
        "profiles": profiles,
        "likely_recipes": recipes,
        "candidate_cross_cutting": components,
        "likely_exclusions": exclusions,
        "reasons": reasons,
        "message": "Project priors only; nothing is activated.",
    }


def command_recommend(args: Namespace) -> int:
    try:
        result = recommend_project(getattr(args, "project", None))
    except (OSError, ValueError) as error:
        print(f"recommend failed: {error}")
        return 1
    if getattr(args, "json", False):
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("Project profiles: " + ", ".join(result["profiles"]))
        print("Likely recipes:")
        for index, slug in enumerate(result["likely_recipes"], 1):
            print(f"  {index}. {slug}")
        print("Candidate cross-cutting components:")
        for slug in result["candidate_cross_cutting"]:
            print(f"  - {slug}")
        print("Nothing is activated. Run: upgradeables task \"<current task>\"")
    return 0


run_recommend = command_recommend
