"""Evaluate concise composition-prior rules over explicit resolver state."""
from __future__ import annotations

from upgradeables_harness.registry.load import load_ontology


def _lookup(context: dict, dotted: str):
    value = context
    for part in dotted.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def _condition_matches(condition: dict, context: dict) -> bool:
    if condition.get("always") is True:
        return True
    if "all" in condition:
        return all(_condition_matches(item, context) for item in condition["all"])
    if "any" in condition:
        return any(_condition_matches(item, context) for item in condition["any"])
    actual = _lookup(context, condition.get("field", ""))
    expected = condition.get("value")
    operator = condition.get("op")
    if operator == "eq":
        return actual == expected
    if operator == "in":
        return actual in expected
    if operator == "exists":
        return (actual is not None) == bool(expected)
    if operator == "gte":
        try:
            return actual >= expected
        except TypeError:
            return False
    return False


def build_context(*, resolution: str, archetype: str | None, subtype: str | None,
                  execution_form: str, environment: dict):
    impact = "high" if environment.get("high_stakes") else (
        "low" if environment.get("simple_exact_edit") else "unknown"
    )
    action = "consequential" if environment.get("irreversible_action") else (
        "no" if environment.get("review_only") else
        "reversible" if environment.get("editing_requested") else "draft-only"
    )
    return {
        "task": {"resolution": resolution, "archetype": archetype,
                 "subtype": subtype, "execution_form": execution_form},
        "modifiers": environment,
        "permissions": environment,
        "capabilities": environment,
        "derived": environment,
        "risk": {"impact_magnitude": impact, "action_requested": action},
    }


def evaluate_priors(context: dict):
    result = {
        "matched_rules": [],
        "recipe_promote": [],
        "recipe_conditional": [],
        "recipe_exclude": [],
        "component_promote": [],
        "component_conditional": [],
        "component_demote": [],
        "component_hard_exclude": [],
        "hard_restrictions": [],
        "required_checks": [],
        "force_no_recipe": False,
    }
    rules = sorted(load_ontology()["composition_priors"]["rules"],
                   key=lambda row: (row["priority"], row["id"]))
    for rule in rules:
        if not _condition_matches(rule["when"], context):
            continue
        result["matched_rules"].append({"id": rule["id"], "reason": rule["reason"]})
        effects = rule["effects"]
        recipes = effects.get("candidate_recipes", {})
        result["recipe_promote"].extend(recipes.get("promote", []))
        result["recipe_conditional"].extend(recipes.get("conditional", []))
        result["recipe_exclude"].extend(recipes.get("exclude", []))
        if recipes.get("force_none"):
            result["force_no_recipe"] = True
        components = effects.get("components", {})
        for key in ("promote", "conditional", "demote", "hard_exclude"):
            result[f"component_{key}"].extend(components.get(key, []))
        result["hard_restrictions"].extend(effects.get("hard_restrictions", []))
        result["required_checks"].extend(effects.get("required_checks", []))
    for key, value in result.items():
        if isinstance(value, list) and key != "matched_rules":
            result[key] = list(dict.fromkeys(value))
    return result
