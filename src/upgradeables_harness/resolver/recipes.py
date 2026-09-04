"""Recipe ranking from task, ontology, environment, and weak project priors."""
from __future__ import annotations

from upgradeables_harness.registry.load import load_ontology, load_profiles, load_recipes
from upgradeables_harness.registry.query import normalize

from .scoring import score_fields


RECIPE_WEIGHTS = {
    "slug": 14,
    "display_name": 8,
    "task_phrases": 12,
    "task_family": 7,
    "purpose": 3,
    "activation_boundary": 2,
}


def _profile_slugs(project: dict | None):
    if not project:
        return []
    explicit = (
        project.get("selected_profiles")
        or project.get("profiles")
        or project.get("preferred_profiles")
        or []
    )
    result = set(explicit)
    mapping = {
        "research-and-knowledge": "research",
        "software-development": "software-development",
        "documentation": "documentation",
        "data-analysis": "data-analysis",
        "medical-evidence": "medical-evidence",
        "legal-evidence": "legal-evidence",
        "agent-development": "agent-development",
    }
    result.update(mapping[value] for value in project.get("project_types", []) if value in mapping)
    if project.get("features", {}).get("long_context"):
        result.add("long-context")
    return sorted(result)


def rank_recipes(query: str, archetype: dict | None, subtype: str | None,
                 environment: dict, project: dict | None, prior_effects: dict | None = None):
    ontology = load_ontology()
    recipes = load_recipes()["recipes"]
    profiles = {item["slug"]: item for item in load_profiles()["profiles"]}
    active_profiles = _profile_slugs(project)
    profile_promote = {
        slug for profile in active_profiles if profile in profiles
        for slug in profiles[profile]["likely_recipes"]
    }
    profile_exclude = {
        slug for profile in active_profiles if profile in profiles
        for slug in profiles[profile]["likely_exclusions"]
    }
    project_task_priors = set(project.get("likely_task_families", [])) if project else set()
    env_records = {}
    source = ontology["environment_modifiers"]
    for group in ("task_environment_modifiers", "permissions", "derived_signals"):
        env_records.update({item["slug"]: item for item in source[group]})
    true_signals = {key for key, value in environment.items() if value is True}
    ranked = []
    prior_effects = prior_effects or {}
    for recipe in recipes:
        score, matched, details = score_fields(query, recipe, RECIPE_WEIGHTS)
        reasons = []
        if normalize(query) == normalize(recipe["slug"]):
            score += 500
            reasons.append("exact recipe slug")
        if archetype and recipe["slug"] in archetype.get("candidate_recipes", []):
            score += 24
            reasons.append(f"candidate for {archetype['slug']}")
        if archetype and recipe["slug"] in archetype.get("normally_excluded_recipes", []):
            score -= 35
            reasons.append(f"normally excluded for {archetype['slug']}")
        if subtype and normalize(subtype).replace(" ", "-") in normalize(
                recipe["task_family"]).replace(" ", "-"):
            score += 12
            reasons.append(f"matches subtype {subtype}")
        if recipe["slug"] in profile_promote:
            score += 8
            reasons.append("weak project-profile prior")
        if recipe["slug"] in project_task_priors:
            score += 6
            reasons.append("project task-map prior")
        if recipe["slug"] in profile_exclude:
            score -= 8
            reasons.append("weak project-profile exclusion")
        # "Review this change" is intentionally under-specified. A research
        # project may use review as source/manuscript evaluation; do not let the
        # generic word "review" force the software-only recipe in that case.
        query_text = normalize(query)
        generic_research_review = (
            "research" in active_profiles
            and "review" in query_text
            and not any(term in query_text for term in (
                "code", "pull request", " pr ", "diff", "commit", "bug", "regression", "api",
                "medical", "clinical", "legal", "law", "regulation",
            ))
        )
        if generic_research_review and recipe["slug"] == "code-review":
            score -= 65
            reasons.append("generic review demoted outside a software signal")
        if generic_research_review and recipe["slug"] == "source-grounded-analysis":
            score += 30
            reasons.append("under-specified review interpreted through research project context")
        if generic_research_review and recipe["slug"] in {"medical-evidence", "legal-evidence"}:
            score -= 20
            reasons.append("specialized evidence domain not stated")
        for signal in sorted(true_signals):
            record = env_records.get(signal, {})
            ranking = record.get("recipe_ranking", {})
            if recipe["slug"] in ranking.get("promote", []):
                score += 10
                reasons.append(f"promoted by {signal}")
            if recipe["slug"] in ranking.get("demote", []):
                score -= 15
                reasons.append(f"demoted by {signal}")
        if recipe["slug"] in prior_effects.get("recipe_promote", []):
            score += 30
            reasons.append("promoted by matched composition prior")
        if recipe["slug"] in prior_effects.get("recipe_conditional", []):
            score += 8
            reasons.append("conditional composition prior")
        if recipe["slug"] in prior_effects.get("recipe_exclude", []):
            score -= 1000
            reasons.append("excluded by matched composition prior")
        ranked.append({
            "slug": recipe["slug"],
            "display_name": recipe["display_name"],
            "score": score,
            "matched": matched,
            "match_details": details,
            "reasons": reasons,
            "recipe": recipe,
        })
    ranked.sort(key=lambda row: (-row["score"], row["slug"]))
    return ranked
