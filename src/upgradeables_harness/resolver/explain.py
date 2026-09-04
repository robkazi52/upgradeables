"""Human rendering for stable resolver output."""
from __future__ import annotations


def render_task(result: dict, *, explain: bool = False) -> str:
    lines = []
    project = result.get("project")
    if project:
        summary = project.get("summary") or ", ".join(project.get("project_types", []))
        lines.extend(["Project:", summary or "detected project", ""])
    best = result.get("best_recipe")
    if not best:
        lines.append("No confident primary recipe.")
        if result.get("candidates"):
            lines.append("Candidates: " + ", ".join(item["slug"] for item in result["candidates"][:3]))
        lines.append("Use a direct path or clarify the task; nothing is activated.")
        return "\n".join(lines) + "\n"
    lines.extend(["Best recipe:", best["slug"], "", "Why:"])
    lines.append("; ".join(best["reasons"] or ["deterministic task match"]))
    labels = (
        ("Required by recipe", "required_by_recipe"),
        ("Trigger-likely", "trigger_likely"),
        ("Conditional", "conditional"),
        ("Optional", "optional"),
        ("Excluded", "excluded"),
        ("Needs agent evaluation", "needs_agent_evaluation"),
    )
    for label, key in labels:
        values = result.get(key, [])
        lines.extend(["", f"{label}:", ", ".join(f"{x['slug']}@{x['version']}" for x in values) or "none"])
    if explain:
        lines.extend(["", "Resolution:",
                      f"archetype={result['task']['archetype'] or 'none'}; "
                      f"complexity={result['complexity']['floor']}..{result['complexity']['ceiling']}"])
    lines.extend(["", "These are selection candidates, not automatic activations."])
    return "\n".join(lines) + "\n"
