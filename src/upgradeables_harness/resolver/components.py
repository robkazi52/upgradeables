"""Resolve one recipe into bounded component candidate groups."""
from __future__ import annotations

from upgradeables_harness.constants import ROLE_GROUPS
from upgradeables_harness.registry.load import load_catalog, load_ontology
from upgradeables_harness.registry.query import normalize, tokens

from .scoring import level_index

MUTATION_COMPONENTS = {
    "micro-repair", "contradiction-micro-repair", "surgery-edit", "crispr-edit",
    "safe-rewrite", "regenerative-rewrite", "external-state-automation",
}


def _trigger_match(query: str, component: dict, environment: dict):
    query_tokens = tokens(query)
    phrases = [*component.get("triggers", []), *component.get("best_fit_tasks", []),
               *component.get("task_phrases", [])]
    matched = sorted({token for phrase in phrases for token in query_tokens & tokens(phrase)})
    promoted = sorted(set(component["selection_prior"].get("environment_promoters", [])) &
                      {key for key, value in environment.items() if value is True})
    return matched, promoted


def resolve_components(query: str, recipe: dict | None, environment: dict, ceiling: str,
                       prior_effects: dict | None = None):
    catalog = {item["slug"]: item for item in load_catalog()["components"]}
    groups = {value: [] for value in ROLE_GROUPS.values()}
    groups["needs_agent_evaluation"] = []
    hard_excluded = set()
    prior_effects = prior_effects or {}
    hard_excluded.update(prior_effects.get("component_hard_exclude", []))
    if environment.get("review_only") is True or environment.get("editing_requested") is False:
        hard_excluded.update(MUTATION_COMPONENTS)
    source = load_ontology()["environment_modifiers"]
    for group in ("task_environment_modifiers", "permissions", "derived_signals"):
        for item in source[group]:
            if environment.get(item["slug"]) is True:
                hard_excluded.update(item.get("exclude_components", []))
    classifications = recipe["classifications"] if recipe else {}
    for slug, role in classifications.items():
        component = catalog[slug]
        prior = component["selection_prior"]
        trigger_matches, promoted = _trigger_match(query, component, environment)
        reasons = []
        target = ROLE_GROUPS[role]
        if slug in hard_excluded:
            target = "excluded"
            reasons.append("hard-excluded by current authority or environment")
        elif role != "R" and level_index(prior["default_complexity_min"]) > level_index(ceiling):
            target = "excluded"
            reasons.append(f"minimum {prior['default_complexity_min']} exceeds complexity ceiling {ceiling}")
        elif role != "R" and slug in prior_effects.get("component_promote", []):
            target = "trigger_likely"
            reasons.append("promoted by matched composition prior; still requires task-time evaluation")
        elif role != "R" and slug in prior_effects.get("component_conditional", []):
            target = "conditional"
            reasons.append("conditional matched composition prior")
        elif role != "R" and slug in prior_effects.get("component_demote", []):
            target = "needs_agent_evaluation"
            reasons.append("demoted by matched composition prior")
        elif role == "A" and not trigger_matches and not promoted:
            target = "needs_agent_evaluation"
            reasons.append("recipe candidate; no deterministic positive trigger observed")
        elif role == "A":
            reasons.append("positive trigger evidence observed; still requires task-time evaluation")
        elif role == "R":
            reasons.append("required by selected recipe")
        elif role == "C":
            reasons.append("conditional recipe role; condition not asserted automatically")
        elif role == "O":
            reasons.append("optional recipe role")
        else:
            reasons.append("excluded by recipe")
        if trigger_matches:
            reasons.append("matched: " + ", ".join(trigger_matches[:5]))
        if promoted:
            reasons.append("promoted by: " + ", ".join(promoted))
        groups[target].append({
            "slug": slug,
            "version": component["version"],
            "plain_display_name": component["plain_display_name"],
            "recipe_role": role,
            "status": target.replace("_", "-"),
            "reasons": reasons,
        })
    for values in groups.values():
        values.sort(key=lambda item: item["slug"])
    already = {item["slug"] for values in groups.values() for item in values}
    additions = (
        ("trigger_likely", prior_effects.get("component_promote", []), "promoted by matched composition prior"),
        ("conditional", prior_effects.get("component_conditional", []), "conditional matched composition prior"),
        ("excluded", prior_effects.get("component_hard_exclude", []), "hard-excluded by matched composition prior"),
    )
    for target, slugs, reason in additions:
        for slug in slugs:
            if slug in already or slug not in catalog:
                continue
            component = catalog[slug]
            prior = component["selection_prior"]
            actual_target = target
            actual_reason = reason
            if target != "excluded" and level_index(prior["default_complexity_min"]) > level_index(ceiling):
                actual_target = "excluded"
                actual_reason = f"minimum {prior['default_complexity_min']} exceeds complexity ceiling {ceiling}"
            groups[actual_target].append({
                "slug": slug,
                "version": component["version"],
                "plain_display_name": component["plain_display_name"],
                "recipe_role": None,
                "status": actual_target.replace("_", "-"),
                "reasons": [actual_reason],
            })
            already.add(slug)
    for values in groups.values():
        values.sort(key=lambda item: item["slug"])
    return groups
