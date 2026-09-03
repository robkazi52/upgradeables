"""Project-level recipe preselection map."""
from __future__ import annotations


def build_task_map(recommendation: dict, features: dict) -> dict:
    recipes = {}
    for index, slug in enumerate(recommendation.get("likely_recipes", [])):
        reasons = list(recommendation.get("reasons", {}).get(slug, []))
        if features.get("tests") and slug in {"coding-debugging", "code-review"}:
            reasons.append("tests detected")
        if features.get("ci") and slug == "code-review":
            reasons.append("CI detected")
        recipes[slug] = {
            "priority": "high" if index < 3 else "medium",
            "reason": list(dict.fromkeys(reasons)) or ["selected project profile"],
        }
    return {
        "schema_version": "1.0.0",
        "registry_version": "0.2.1",
        "selection_only": True,
        "recipes": recipes,
    }
