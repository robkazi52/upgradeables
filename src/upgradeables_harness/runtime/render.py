"""Human-readable runtime plan renderers."""
from __future__ import annotations


def render_plan(plan: dict, *, explain: bool = False) -> str:
    if not explain:
        return plan["instruction_capsule"] + ("\n" if plan["instruction_capsule"] else "")
    lines = [
        f"Task archetype: {plan['task']['archetype'] or 'unresolved'}",
        f"Task subtype: {plan['task']['subtype'] or 'none'}",
        f"Failure modes: {', '.join(item['slug'] for item in plan['failure_modes']) or 'none'}",
        f"Complexity: {plan['complexity']['floor']}..{plan['complexity']['ceiling']}",
        f"Model profile: {plan['model_profile']}",
        f"Approximate directive tokens: {plan['token_estimate']}",
        "Components:",
    ]
    for item in plan["components"]:
        lines.append(f"- {item['slug']}@{item['version']}: {item['runtime_form']} / {item['runtime_level']}")
    if plan["excluded_runtime_components"]:
        lines.append("Excluded runtime components:")
        lines.extend(f"- {item['slug']}: {item['reason']}" for item in plan["excluded_runtime_components"])
    if plan["decisions"]:
        lines.append("Compiler decisions:")
        lines.extend(f"- {item}" for item in plan["decisions"])
    if plan["directive_provenance"]:
        lines.append("Directive provenance:")
        for item in plan["directive_provenance"]:
            status = "emitted" if item["emitted"] else f"suppressed ({item['suppression_reason']})"
            lines.append(f"- [{status}] {item['text']} <- {item['component']}@{item['version']} ({item['runtime_form']}/{item['runtime_level']})")
    if plan["warnings"]:
        lines.append("Warnings:")
        lines.extend(f"- {item}" for item in plan["warnings"])
    lines.extend(("", plan["instruction_capsule"]))
    return "\n".join(lines).rstrip() + "\n"
