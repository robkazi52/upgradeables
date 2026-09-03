"""Research-ontology-driven deterministic task resolution."""
from __future__ import annotations

import json
import re
from pathlib import Path

from upgradeables_harness.registry.load import load_ontology
from upgradeables_harness.registry.query import normalize, tokens

from .components import resolve_components
from .recipes import rank_recipes
from .priors import build_context, evaluate_priors
from .scoring import level_index, score_fields

ARCHETYPE_HINTS = {
    "knowledge-explanation": (r"\b(explain|teach|what is|how does|tutorial)\b", 45),
    "content-understanding": (r"\b(summarize|extract|understand|analy[sz]e).*(document|pdf|corpus|text)\b", 50),
    "content-transformation": (r"\b(rewrite|translate|convert|rename|reformat|preserv)\b", 50),
    "content-authoring": (r"\b(write|draft|author|publication|article|documentation)\b", 40),
    "research-grounding": (r"\b(research|sources?|citations?|evidence|literature|papers?|regulation|clinical)\b", 48),
    "quantitative-analysis": (r"\b(data|dataset|calculate|statistics?|quantitative|spreadsheet|csv)\b", 42),
    "constraint-reasoning": (r"\b(puzzle|constraint|grid|logic|optimal|solve)\b", 40),
    "planning-design": (r"\b(plan|design|architecture|strategy|roadmap)\b", 43),
    "decision-support": (r"\b(decide|choose|compare options|tradeoffs?|recommend)\b", 45),
    "creative-exploration": (r"\b(brainstorm|creative|ideas?|concepts?|directions?)\b", 48),
    "software-engineering": (r"\b(code|repository|pull request|\bpr\b|diff|bug|test|debug|implement|refactor|api)\b", 45),
    "evaluation-audit": (r"\b(review|audit|evaluate|verify|check|regressions?|find bugs)\b", 52),
    "action-execution": (r"\b(deploy|send|publish|execute|delete|purchase|transact)\b", 45),
    "workflow-automation": (r"\b(automate|routing|route|intake|workflow from fields)\b", 48),
    "skill-agent-creation": (r"\b(build|create|design|improve).*(skill|agent|prompt|workflow)\b", 58),
}

SUBTYPE_HINTS = (
    (r"pull request|\bpr\b|diff|patch.*review|review.*patch", "code-review"),
    (r"fix|repair|failing test", "localized-repair"),
    (r"debug|diagnos|reproduce", "bug-diagnosis"),
    (r"refactor", "behavior-preserving-refactor"),
    (r"architecture|system design", "architecture-design"),
    (r"rewrite|transform", "constrained-rewrite"),
    (r"summari[sz]", "summarization"),
    (r"source|evidence|citation", "source-bounded-qa"),
    (r"skill", "skill-creation"),
    (r"brainstorm|ideas", "divergent-ideation"),
)


def _tri_state_catalog():
    source = load_ontology()["environment_modifiers"]
    return [item["slug"] for group in (
        "task_environment_modifiers", "host_capabilities", "permissions", "derived_signals"
    ) for item in source[group]]


def detect_environment(task: str):
    text = normalize(task)
    result = {slug: None for slug in _tri_state_catalog()}
    review_only = bool(re.search(r"\b(review only|do not (edit|modify|change)|without (editing|modifying)|no edits?)\b", text))
    edit = bool(re.search(r"\b(fix|implement|edit|modify|refactor|rename|rewrite|update|apply patch)\b", text))
    result.update({
        "review_only": review_only,
        "editing_requested": False if review_only else (True if edit else None),
        "has_supplied_sources": True if re.search(r"\b(these|provided|supplied|attached) (sources|documents|files|papers)\b", text) else None,
        "requires_citations": False if re.search(r"\b(no|without) citations?\b", text) else (True if re.search(r"\b(cite|citation|sources with links)\b", text) else None),
        "long_context": True if re.search(r"\b(long|large) (document|pdf|corpus|context)|many documents|across (the )?corpus\b", text) else None,
        "multi_document": True if re.search(r"\b(multiple|many|several|five|[2-9]) (sources|documents|papers|files)\b", text) else None,
        "requires_exact_fidelity": True if re.search(r"\b(exact|verbatim|preserv(e|ing)|unchanged|fidelity)\b", text) else None,
        "contains_protected_literals": True if re.search(r"\b(preserve|keep).*(numbers?|dates?|quotes?|identifiers?)\b", text) else None,
        "structured_output_required": True if re.search(r"\b(json|schema|table|csv|structured output)\b", text) else None,
        "high_stakes": True if re.search(r"\b(medical|clinical|legal|financial|security|production|safety|rights?)\b", text) else None,
        "time_sensitive": True if re.search(r"\b(latest|current|today|recent|deadline|urgent)\b", text) else None,
        "tools_required": True if re.search(r"\b(run|execute|browse|search the web|test suite|inspect the repo)\b", text) else None,
        "persistent_work": True if re.search(r"\b(resume|continue|multi session|long running|persistent)\b", text) else None,
        "irreversible_action": True if re.search(r"\b(delete|deploy|publish|purchase|send|irreversible|production)\b", text) else None,
        "external_action_allowed": True if re.search(r"\b(deploy|publish|send|purchase)\b", text) else None,
        "acceptance_criteria_present": True if re.search(r"\b(acceptance criteria|done when|must pass)\b", text) else None,
        "reproduction_available": True if re.search(r"\b(repro|reproduce|failing test)\b", text) else None,
        "context_window_pressure": True if re.search(r"\b(long|large) (document|corpus|context)|many documents\b", text) else None,
        "evidence_conflicting": True if re.search(r"\b(conflicting|disagree|contradictory) (evidence|sources|studies)\b", text) else None,
    })
    simple = bool(re.search(r"\brename\b.*\b(to|from)\b|\b(one|single) (word|heading|label|literal)\b", text))
    result["simple_exact_edit"] = True if simple else None
    return result


def classify_archetype(task: str):
    archetypes = load_ontology()["task_archetypes"]["archetypes"]
    text = normalize(task)
    ranked = []
    for record in archetypes:
        score, matched, details = score_fields(task, record, {
            "slug": 8, "display_name": 4, "description": 1, "subtypes": 7,
            "common_user_phrases": 9, "representative_tasks": 4,
            "input_patterns": 1, "output_patterns": 1,
        })
        pattern, bonus = ARCHETYPE_HINTS[record["slug"]]
        if re.search(pattern, text):
            score += bonus
            matched.append("task-pattern")
        ranked.append({"slug": record["slug"], "score": score,
                       "matched": sorted(set(matched), key=str.casefold),
                       "match_details": details, "record": record})
    ranked.sort(key=lambda item: (-item["score"], item["slug"]))
    top = ranked[0]
    if top["score"] < 18:
        return None, ranked[:3]
    return top, ranked[:3]


def _subtype(task: str, archetype: dict | None):
    text = normalize(task)
    allowed = set(archetype.get("subtypes", [])) if archetype else set()
    for pattern, value in SUBTYPE_HINTS:
        if re.search(pattern, text) and value in allowed:
            return value
    for value in sorted(allowed):
        if normalize(value) in text:
            return value
    return None


def _execution_form(environment: dict, task: str):
    text = normalize(task)
    if re.search(r"multiple agents|parallel workers|delegate", text):
        return "orchestrated-workers"
    if environment.get("persistent_work"):
        return "stateful-continuation"
    if environment.get("tools_required"):
        return "tool-assisted"
    if re.search(r"workflow|steps|pipeline", text):
        return "fixed-workflow"
    return "direct-response"


def _complexity(archetype: dict | None, environment: dict, execution_form: str):
    reasons = []
    if not archetype:
        return {"floor": "L0", "ceiling": "L1", "reasons": ["no-match direct-or-clarify policy"]}
    floor = archetype["default_complexity_floor"]
    ceiling = archetype["default_complexity_ceiling"]
    if environment.get("simple_exact_edit"):
        floor, ceiling = "L0", "L1"
        reasons.append("simple exact edit hard suppression")
    if environment.get("review_only") and level_index(ceiling) > 2:
        ceiling = "L2"
        reasons.append("bounded review-only task")
    if environment.get("long_context") or environment.get("multi_document"):
        if level_index(floor) < 2:
            floor = "L2"
        if level_index(ceiling) < 2:
            ceiling = "L2"
        reasons.append("distributed or long-context evidence")
    if environment.get("high_stakes"):
        if level_index(floor) < 2:
            floor = "L2"
        if level_index(ceiling) < 3:
            ceiling = "L3"
        reasons.append("high-stakes consequence")
    if environment.get("irreversible_action"):
        if level_index(floor) < 3:
            floor = "L3"
        if level_index(ceiling) < 4:
            ceiling = "L4"
        reasons.append("irreversible or external action")
    if execution_form == "orchestrated-workers":
        floor = ceiling = "L5"
        reasons.append("explicit multi-worker execution request")
    if level_index(floor) > level_index(ceiling):
        ceiling = floor
    if not reasons:
        reasons.append(f"default bound for {archetype['slug']}")
    return {"floor": floor, "ceiling": ceiling, "reasons": reasons}


def _failure_modes(archetype: dict | None, environment: dict):
    observed = []
    def add(slug, reason):
        if slug not in {item["slug"] for item in observed}:
            observed.append({"slug": slug, "reason": reason})
    if environment.get("review_only"):
        add("over-editing", "task explicitly denies edit authority")
        add("mode-scope-authority-drift", "review authority must remain read-only")
    if environment.get("requires_exact_fidelity") or environment.get("contains_protected_literals"):
        add("constraint-loss", "protected fidelity constraints are explicit")
        add("invariant-violation", "protected values or meaning could change")
    if environment.get("requires_citations"):
        add("citation-source-mismatch", "claim-level citation support is requested")
        add("evidence-coverage-gap", "required claims may lack source coverage")
    if environment.get("has_supplied_sources") or environment.get("multi_document"):
        add("unsupported-claim", "claims must remain within an evidence boundary")
    if environment.get("long_context") or environment.get("context_window_pressure"):
        add("context-overload", "relevant material may exceed focused context")
        add("lost-state", "long work may lose task or evidence state")
    if environment.get("high_stakes"):
        add("under-verification", "consequential result needs proportionate validation")
        add("poor-uncertainty-handling", "uncertainty may materially affect the result")
    if not observed and archetype:
        common = archetype.get("common_failure_modes", [])
        if common:
            add(common[0], f"common risk for {archetype['slug']}; not asserted as observed")
    return observed


def _read_project(project):
    if isinstance(project, dict):
        return project
    if project is None:
        return None
    path = Path(project).expanduser().resolve()
    candidate = path if path.name == "project.json" else path / ".upgradeables" / "project.json"
    if candidate.is_file():
        return json.loads(candidate.read_text(encoding="utf-8"))
    return None


def resolve_task(task: str, project: dict | str | Path | None = None,
                 use_project_profile: bool = True) -> dict:
    if not task or not task.strip():
        raise ValueError("task must not be empty")
    project_data = _read_project(project) if use_project_profile else None
    environment = detect_environment(task)
    classification, alternatives = classify_archetype(task)
    archetype = classification["record"] if classification else None
    subtype = _subtype(task, archetype)
    execution_form = _execution_form(environment, task)
    complexity = _complexity(archetype, environment, execution_form)
    preliminary_resolution = "matched" if classification else "no-match"
    prior_effects = evaluate_priors(build_context(
        resolution=preliminary_resolution,
        archetype=classification["slug"] if classification else None,
        subtype=subtype,
        execution_form=execution_form,
        environment=environment,
    ))
    ranked = rank_recipes(task, archetype, subtype, environment, project_data, prior_effects)
    threshold = 30
    best_rank = ranked[0] if ranked and ranked[0]["score"] >= threshold and archetype else None
    # No current recipe is a genuinely minimal literal-edit recipe. Returning no
    # recipe is more honest than promoting the broader authoring stack.
    if environment.get("simple_exact_edit"):
        best_rank = None
    if prior_effects["force_no_recipe"]:
        best_rank = None
    groups = {key: [] for key in (
        "required_by_recipe", "trigger_likely", "conditional", "optional", "excluded",
        "needs_agent_evaluation",
    )}
    best = None
    if best_rank:
        best = {key: best_rank[key] for key in ("slug", "display_name", "score", "matched", "reasons")}
        groups = resolve_components(task, best_rank["recipe"], environment, complexity["ceiling"], prior_effects)
        if environment.get("requires_citations") is False:
            for key in ("conditional", "trigger_likely", "needs_agent_evaluation", "optional"):
                moved = [item for item in groups[key] if item["slug"] == "citation-fidelity"]
                groups[key] = [item for item in groups[key] if item["slug"] != "citation-fidelity"]
                for item in moved:
                    item["status"] = "excluded"
                    item["reasons"] = ["explicitly requested no citations"]
                    groups["excluded"].append(item)
            groups["excluded"].sort(key=lambda item: item["slug"])
    else:
        groups = resolve_components(task, None, environment, complexity["ceiling"], prior_effects)
    task_record = {
        "resolution": "matched" if best else ("ambiguous" if classification else "no-match"),
        "archetype": classification["slug"] if classification else None,
        "archetype_score": classification["score"] if classification else 0,
        "subtype": subtype,
        "execution_form": execution_form,
        "matched": classification["matched"] if classification else [],
    }
    result = {
        "schema_version": "1.0.0",
        "registry_version": "0.2.1",
        "selection_only": True,
        "query": task,
        "normalized_task": normalize(task),
        "project": project_data,
        "task": task_record,
        "environment": environment,
        "failure_modes": _failure_modes(archetype, environment),
        "complexity": complexity,
        "matched_prior_rules": prior_effects["matched_rules"],
        "hard_restrictions": prior_effects["hard_restrictions"],
        "required_checks": prior_effects["required_checks"],
        "best_recipe": best,
        "candidates": [
            {key: item[key] for key in ("slug", "display_name", "score", "matched", "reasons")}
            for item in ranked[:3] if item["score"] > 0
        ],
        **groups,
        "archetype_alternatives": [
            {key: item[key] for key in ("slug", "score", "matched")} for item in alternatives
        ],
        "activation_note": "Selection priors only. Evaluate current triggers, non-triggers, dependencies, conflicts, counterbalances, authority, and the complexity ceiling before activation.",
    }
    return result
