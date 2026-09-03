"""Find low-context Upgradeable runtime material with deterministic matching."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "registry/catalog.json"
RUNTIME_INDEX = ROOT / "runtime/index.json"
STOPWORDS = {
    "a", "an", "and", "are", "for", "from", "i", "in", "is", "it", "me",
    "my", "of", "on", "or", "please", "the", "this", "to", "with",
}


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(value):
    return " ".join(re.findall(r"[a-z0-9]+", value.casefold()))


def tokens(value):
    result = set()
    for token in normalize(value).split():
        if token in STOPWORDS:
            continue
        result.add(token)
        if len(token) > 4 and token.endswith("s"):
            result.add(token[:-1])
        if len(token) > 5 and token.endswith("ing"):
            result.add(token[:-3])
    return result


def values(record, fields):
    result = []
    for field in fields:
        value = record.get(field, "")
        result.extend(value if isinstance(value, list) else [value])
    return [str(value) for value in result if value]


def match_details(query, record, fields):
    query_text = normalize(query)
    query_tokens = tokens(query)
    matched = set()
    score = 0
    for field, weight in fields.items():
        for value in values(record, [field]):
            normalized = normalize(value)
            overlap = query_tokens & tokens(value)
            if normalized and (normalized in query_text or query_text in normalized):
                score += weight * 4
                matched.add(value)
            if overlap:
                score += weight * len(overlap)
                matched.update(sorted(overlap))
    return score, sorted(matched, key=str.casefold)[:6]


def brief_component(record):
    return {
        "kind": "component",
        "slug": record["slug"],
        "name": record["name"],
        "purpose": record["purpose"],
        "trigger": record["trigger"],
        "avoid": record["avoid"],
        "runtime_path": record["path"],
    }


def brief_recipe(record, catalog_recipe):
    return {
        "kind": "recipe",
        "slug": record["slug"],
        "name": record["name"],
        "purpose": record["purpose"],
        "task_family": record["task_family"],
        "runtime_path": record["path"],
        "components": [
            {
                "slug": item["slug"],
                "role": item["role"],
                "name": item.get("plain_display_name", item["display_name"]),
                "trigger": item["trigger_summary"],
            }
            for item in catalog_recipe["components"]
        ],
    }


def task_result(query, runtime, catalog):
    recipe_fields = {"name": 7, "task_phrases": 10, "task_family": 6, "purpose": 4}
    skill_fields = {"slug": 6, "task_phrases": 10, "description": 4}
    ranked_recipes = []
    for recipe in runtime["recipes"]:
        score, matched = match_details(query, recipe, recipe_fields)
        if score:
            ranked_recipes.append((score, recipe["slug"], matched, recipe))
    ranked_recipes.sort(key=lambda row: (-row[0], row[1]))
    ranked_skills = []
    for skill in runtime["skills"]:
        score, matched = match_details(query, skill, skill_fields)
        if score:
            ranked_skills.append((score, skill["slug"], matched, skill))
    ranked_skills.sort(key=lambda row: (-row[0], row[1]))

    if not ranked_recipes:
        return {
            "query": query,
            "best_recipe": None,
            "existing_skills": [],
            "reason": "No recipe had a meaningful deterministic match; answer directly or refine the task.",
        }

    score, _, matched, recipe = ranked_recipes[0]
    catalog_recipe = next(item for item in catalog["recipes"] if item["slug"] == recipe["slug"])
    role_names = {"R": "required", "A": "likely", "C": "conditional", "O": "optional", "X": "excluded"}
    groups = {value: [] for value in role_names.values()}
    for component in catalog_recipe["components"]:
        groups[role_names[component["role"]]].append({
            "slug": component["slug"],
            "name": component.get("plain_display_name", component["display_name"]),
            "trigger": component["trigger_summary"],
            "runtime_path": f"runtime/components/{component['slug']}.md",
        })
    skills = [{
        "slug": skill["slug"],
        "description": skill["description"],
        "matched": skill_matched,
        "path": skill["path"],
    } for skill_score, _, skill_matched, skill in ranked_skills[:3] if skill_score >= 20]
    return {
        "query": query,
        "best_recipe": {
            "slug": recipe["slug"],
            "name": recipe["name"],
            "score": score,
            "matched": matched,
            "why": f"Matched {', '.join(matched) if matched else recipe['task_family']}.",
            "runtime_path": recipe["path"],
        },
        "existing_skills": skills,
        **groups,
        "activation_note": "R owns a required guarantee but may wait for its phase. A/C/O still require active triggers; X stays excluded without a specific reason.",
    }


def apply_fields(result, requested):
    fields = [field.strip() for field in requested.split(",") if field.strip()]
    def project(item):
        return {field: item[field] for field in fields if field in item}
    return [project(item) for item in result] if isinstance(result, list) else project(result)


def result_paths(result):
    if isinstance(result, list):
        return [item.get("runtime_path") or item.get("path") or item.get("package_path") for item in result]
    if result.get("best_recipe") is not None:
        paths = [result["best_recipe"]["runtime_path"]]
        paths.extend(item["path"] for item in result.get("existing_skills", []))
        return paths
    return [result.get("runtime_path") or result.get("path") or result.get("package_path")]


def render_task_text(result):
    if not result.get("best_recipe"):
        return f"No confident recipe match. {result['reason']}\n"
    best = result["best_recipe"]
    lines = [f"Best recipe: {best['slug']}", f"Why: {best['why']}"]
    if result["existing_skills"]:
        lines.append("Existing Skills: " + ", ".join(item["slug"] for item in result["existing_skills"]))
    for key in ("required", "likely", "conditional", "optional", "excluded"):
        selected = ", ".join(item["slug"] for item in result[key]) or "none"
        lines.append(f"{key.title()}: {selected}")
    lines.append(f"Load: {best['runtime_path']}")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    selectors = parser.add_mutually_exclusive_group(required=True)
    selectors.add_argument("--slug", help="exact Upgradeable slug")
    selectors.add_argument("--recipe", help="exact recipe slug")
    selectors.add_argument("--class", dest="functional_class", help="functional class")
    selectors.add_argument("--search", help="normalized search across components, recipes, and Skills")
    selectors.add_argument("--task", help="natural-language task discovery")
    parser.add_argument("--brief", action="store_true", help="return the low-context projection")
    parser.add_argument("--runtime", action="store_true", help="emit selected runtime Markdown")
    parser.add_argument("--limit", type=int, default=10, help="maximum list results; 0 means unlimited")
    parser.add_argument("--fields", help="comma-separated top-level output fields")
    parser.add_argument("--paths-only", action="store_true")
    parser.add_argument("--explain", action="store_true", help="include normalized match evidence")
    parser.add_argument("--format", choices=("json", "text"), default="json")
    parser.add_argument("--compact", action="store_true", help="minify JSON output")
    args = parser.parse_args()
    if args.limit < 0:
        parser.error("--limit cannot be negative")
    if args.fields and args.paths_only:
        parser.error("--fields and --paths-only cannot be combined")

    catalog = load(CATALOG)
    runtime = load(RUNTIME_INDEX)
    component_runtime = {item["slug"]: item for item in runtime["components"]}
    recipe_runtime = {item["slug"]: item for item in runtime["recipes"]}

    if args.slug:
        full = next((item for item in catalog["upgradeables"] if item["slug"] == args.slug), None)
        result = brief_component(component_runtime[args.slug]) if full and args.brief else full
        runtime_path = component_runtime.get(args.slug, {}).get("path")
    elif args.recipe:
        full = next((item for item in catalog["recipes"] if item["slug"] == args.recipe), None)
        result = brief_recipe(recipe_runtime[args.recipe], full) if full and args.brief else full
        runtime_path = recipe_runtime.get(args.recipe, {}).get("path")
    elif args.functional_class:
        result = [brief_component(component_runtime[item["slug"]]) if args.brief else item for item in catalog["upgradeables"] if args.functional_class in item["functional_classes"]]
        runtime_path = None
    elif args.search:
        query = normalize(args.search)
        result = []
        for kind, records in (("component", runtime["components"]), ("recipe", runtime["recipes"]), ("skill", runtime["skills"])):
            for record in records:
                haystack = normalize(" ".join(values(record, record.keys())))
                if query in haystack:
                    item = {"kind": kind, **record}
                    if args.explain:
                        item["matched"] = args.search
                    result.append(item)
        result.sort(key=lambda item: (item["kind"], item["slug"]))
        runtime_path = None
    else:
        result = task_result(args.task, runtime, catalog)
        runtime_path = result.get("best_recipe", {}).get("runtime_path") if result.get("best_recipe") else None

    if result is None:
        print(json.dumps({"error": "not found"}, indent=2), file=sys.stderr)
        return 1
    if isinstance(result, list) and args.limit:
        result = result[:args.limit]
    if args.runtime:
        if not runtime_path:
            parser.error("--runtime requires a matched --slug, --recipe, or --task")
        sys.stdout.write((ROOT / runtime_path).read_text(encoding="utf-8"))
        return 0
    if args.paths_only:
        result = result_paths(result)
    if args.fields:
        result = apply_fields(result, args.fields)
    if args.format == "text" and args.task and not args.paths_only and not args.fields:
        sys.stdout.write(render_task_text(result))
    elif args.format == "text":
        for item in result if isinstance(result, list) else [result]:
            print(item if isinstance(item, str) else f"{item.get('kind', 'item')}: {item.get('slug', item.get('name', 'result'))}")
    else:
        separators = (",", ":") if args.compact else None
        print(json.dumps(result, ensure_ascii=False, indent=None if args.compact else 2, separators=separators))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
