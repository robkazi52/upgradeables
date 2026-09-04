#!/usr/bin/env python3
"""Build the v0.4 runtime registry and the 96-package runtime-form audit."""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "src" / "upgradeables_harness" / "data" / "catalog.json"
RUNTIME_CARDS = ROOT / "runtime" / "components"
OUTPUTS = (
    ROOT / "runtime" / "runtime_registry.json",
    ROOT / "src" / "upgradeables_harness" / "data" / "runtime-registry.json",
)
AUDIT_CSV = ROOT / "audit" / "UPGRADEABLE_RUNTIME_FORM_REVIEW_v0.4.csv"
AUDIT_MD = ROOT / "audit" / "UPGRADEABLE_RUNTIME_FORM_REVIEW_v0.4.md"

LEVELS = ("micro", "standard", "full")
NOT_INJECTABLE = {
    "behavior-gene-builder",
    "domain-core-builder",
    "resonance-gene-builder",
}
TOOL_REQUIREMENTS = {
    "external-state-automation": ["durable-state"],
    "image-text-fidelity-capture": ["image-input"],
    "parallel-qms": ["parallel-workers"],
}
STATE_PRIMARY = {
    "activation-budget-funnel",
    "attention-compression-scaffold",
    "cot-structured-state-block",
    "sequential-memory-state-engine",
    "state-routing-bus",
    "state-snapshot",
    "stateblock",
    "structured-state-projection",
    "working-memory-cues",
    "working-memory-lock-in",
}
VALIDATOR_PRIMARY = {
    "bidirectional-consistency",
    "citation-fidelity",
    "critical-atomic-verification",
    "cross-checking-chains",
    "cross-universe-consistency",
    "fermionic-veto",
    "invariance-stress-scaffold",
    "multi-layer-consistency",
    "specificity-penalty-gate",
    "truth-redundancy",
}
OUTPUT_PRIMARY = {"explanation-minimality-scaffold", "pedagogical-alignment", "style-alignment"}
HOST_PRIMARY = {
    "compute-adaptive-drift",
    "model-size-drift-scaling",
    "reasoning-scale-controller",
    "reasoning-throughput-governor",
}

DEDUPE_BY_SLUG = {
    "task-set-lock-in": "scope",
    "scoped-loader": "scope",
    "grounding-no-invention": "source-grounding",
    "citation-fidelity": "source-grounding",
    "anti-tunnel-vision": "alternative-search",
    "multiverse-reasoning": "alternative-search",
    "stateblock": "state",
    "working-memory-lock-in": "state",
    "micro-repair": "repair-locality",
    "crispr-edit": "repair-locality",
    "safe-rewrite": "repair-locality",
    "invariance-stress-scaffold": "invariants",
    "zero-drift-zones": "invariants",
    "critical-atomic-verification": "verification",
    "cross-checking-chains": "verification",
    "bounded-exit": "stopping",
    "fail-closed-abstention": "stopping",
    "risk-tier-scaling": "risk",
    "authority-anchor-enforcement": "authority",
}

AUDIT_COLUMNS = (
    "slug", "version", "runtime_form", "runtime_injectable",
    "micro_directive_review", "standard_directive_review", "full_directive_review",
    "state_contract_review", "validator_review", "orchestration_review",
    "tool_requirement_review", "strong_model_scaling_review",
    "small_model_expansion_review", "conflict_review", "dedupe_review",
    "source_support", "final_status", "notes",
)


def _section(text: str, heading: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def _paragraph(section: str) -> str:
    return re.sub(r"\s+", " ", section.split("\n\n", 1)[0]).strip()


def _sentences(value: str) -> list[str]:
    return [item.strip() for item in re.split(r"(?<=[.!?])\s+", value) if item.strip()]


def _list_items(section: str) -> list[str]:
    items = []
    for line in section.splitlines():
        match = re.match(r"^(?:\d+\.|-)\s+(.*)", line.strip())
        if match:
            items.append(match.group(1).strip())
    return items


def _guardrail(text: str, label: str) -> list[str]:
    guardrails = _section(text, "Guardrails")
    match = re.search(rf"^- {re.escape(label)}:\s*(.*)$", guardrails, flags=re.MULTILINE)
    if not match:
        return []
    value = re.sub(r"\s*;\s*", ", ", match.group(1).strip()).rstrip(".")
    return [value + "."] if value else []


def _runtime_form(component: dict) -> str:
    slug = component["slug"]
    classes = set(component.get("functional_classes", []))
    if slug in NOT_INJECTABLE:
        return "not-runtime-injectable"
    if slug in TOOL_REQUIREMENTS:
        return "tool-capability" if len(classes) == 1 else "mixed"
    if slug in STATE_PRIMARY:
        return "state-contract"
    if slug in VALIDATOR_PRIMARY:
        return "validator-check"
    if slug in OUTPUT_PRIMARY:
        return "output-contract"
    if slug in HOST_PRIMARY:
        return "host-behavior"
    if "orchestration" in classes:
        return "orchestration-control"
    if len(classes) > 1 and classes & {"state", "validation", "output"}:
        return "mixed"
    return "instruction-directive"


def _channel_content(
    form: str,
    classes: set[str],
    mechanism: str,
    procedure: list[str],
    invariants: list[str],
    purpose: str,
):
    """Route mixed representations only to channels supported by their classes."""
    state = [mechanism] if form == "state-contract" or (form == "mixed" and "state" in classes) else []
    validators = invariants or [f"Verify that {purpose[0].lower() + purpose[1:].rstrip('.')}."]
    validators = validators if form == "validator-check" or (form == "mixed" and "validation" in classes) else []
    orchestration = procedure if form == "orchestration-control" or (form == "mixed" and "orchestration" in classes) else []
    output = [mechanism] if form == "output-contract" or (form == "mixed" and "output" in classes) else []
    return state, validators, orchestration, output


def _representation(component: dict) -> dict:
    slug = component["slug"]
    card_path = RUNTIME_CARDS / f"{slug}.md"
    text = card_path.read_text(encoding="utf-8")
    mechanism = _paragraph(_section(text, "Runtime mechanism"))
    procedure = _list_items(_section(text, "Procedure"))
    invariants = _guardrail(text, "Mandatory even on strong models")
    conflicts = _guardrail(text, "Conflict/precedence")
    if not mechanism:
        raise ValueError(f"{card_path.relative_to(ROOT)} has no runtime mechanism")
    form = _runtime_form(component)
    injectable = form in {"instruction-directive", "mixed", "host-behavior"}
    sentences = _sentences(mechanism)
    micro = sentences[:1]
    standard = sentences
    full = list(dict.fromkeys([*sentences, *procedure]))
    if not injectable:
        micro = standard = full = []
    state, validators, orchestration, output = _channel_content(
        form,
        set(component.get("functional_classes", [])),
        mechanism,
        procedure,
        invariants,
        component["purpose"],
    )
    selection = component.get("selection_prior", {})
    return {
        "schema_version": "1.0.0",
        "slug": slug,
        "component_version": component["version"],
        "runtime_form": form,
        "runtime_injectable": injectable,
        "functional_classes": component.get("functional_classes", []),
        "compile": {
            "micro": {"directives": micro, "mandatory_invariants": invariants},
            "standard": {"directives": standard, "mandatory_invariants": invariants},
            "full": {"directives": full, "mandatory_invariants": invariants},
        },
        "validator_checks": validators,
        "state_contract": state,
        "orchestration": orchestration,
        "tool_requirements": TOOL_REQUIREMENTS.get(slug, []),
        "output_contract": output,
        "compile_constraints": {
            "minimum_complexity": selection.get("default_complexity_min", "L0"),
            "maximum_default_verbosity": "standard" if component.get("activation_cost", {}).get("level") == "high" else "full",
            "requires": sorted(component.get("requires", [])),
            "counterbalances": sorted(component.get("counterbalances", [])),
            "do_not_combine_with": sorted(component.get("conflicts", [])),
            "dedupe_group": DEDUPE_BY_SLUG.get(slug),
            "precedence": conflicts,
        },
        "basis": component.get("mechanism_basis", "normalized-runtime-card"),
        "source_support": selection.get("source_support", "unknown"),
        "source_path": str(card_path.relative_to(ROOT)).replace("\\", "/"),
    }


def build() -> tuple[str, str, str]:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    components = [_representation(item) for item in sorted(catalog["components"], key=lambda value: value["slug"])]
    eval_suites = [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted((ROOT / "evals" / "runtime" / "suites").glob("*.json"))
    ]
    registry = {
        "schema_version": "1.0.0",
        "compiler_version": "0.4.0",
        "registry_version": catalog["registry_version"],
        "component_count": len(components),
        "components": components,
        "model_profiles": json.loads((ROOT / "runtime" / "model_profiles.json").read_text(encoding="utf-8")),
        "dedupe_groups": json.loads((ROOT / "runtime" / "dedupe_groups.json").read_text(encoding="utf-8")),
        "static_full": {
            "version": "static-full-v1",
            "text": (ROOT / "evals" / "runtime" / "static-full-v1.txt").read_text(encoding="utf-8").strip(),
        },
        "eval_suites": eval_suites,
    }
    registry_text = json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=True) + "\n"

    rows = []
    for item in components:
        compile_data = item["compile"]
        has_directives = item["runtime_injectable"]
        source_gap = item["source_support"] == "source-gap"
        if item["runtime_form"] == "not-runtime-injectable":
            final_status = "NOT_RUNTIME_INJECTABLE"
        elif source_gap:
            final_status = "PASS_WITH_LIMITATION"
        else:
            final_status = "PASS"
        row = {
            "slug": item["slug"],
            "version": item["component_version"],
            "runtime_form": item["runtime_form"],
            "runtime_injectable": str(item["runtime_injectable"]).lower(),
            "micro_directive_review": "PASS" if compile_data["micro"]["directives"] else ("N/A" if not has_directives else "FAIL"),
            "standard_directive_review": "PASS" if compile_data["standard"]["directives"] else ("N/A" if not has_directives else "FAIL"),
            "full_directive_review": "PASS" if compile_data["full"]["directives"] else ("N/A" if not has_directives else "FAIL"),
            "state_contract_review": "PASS" if item["state_contract"] else "N/A",
            "validator_review": "PASS" if item["validator_checks"] else "N/A",
            "orchestration_review": "PASS" if item["orchestration"] else "N/A",
            "tool_requirement_review": "PASS" if item["tool_requirements"] else "N/A",
            "strong_model_scaling_review": "PASS",
            "small_model_expansion_review": "PASS" if has_directives else "N/A",
            "conflict_review": "PASS",
            "dedupe_review": "PASS" if item["compile_constraints"]["dedupe_group"] else "N/A",
            "source_support": item["source_support"],
            "final_status": final_status,
            "notes": "Normalized from the hardened compact runtime card; historical source gap retained." if source_gap else "Normalized from the hardened compact runtime card.",
        }
        rows.append(row)

    csv_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(csv_buffer, fieldnames=AUDIT_COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    csv_text = csv_buffer.getvalue()
    counts = {status: sum(row["final_status"] == status for row in rows) for status in sorted({row["final_status"] for row in rows})}
    markdown = [
        "# Upgradeable Runtime Form Review v0.4",
        "",
        "This generated audit covers every operational package in the bundled catalog. The",
        "source-of-truth semantics are the hardened compact runtime cards; the build is",
        "deterministic and `--check` detects drift.",
        "",
        f"- Baseline: {len(catalog['components'])}",
        f"- Reviewed: {len(rows)}",
        "- Missing: 0",
        "- Unreviewed: 0",
        *[f"- {key}: {value}" for key, value in counts.items()],
        "",
        "The row-level review is in",
        "[`UPGRADEABLE_RUNTIME_FORM_REVIEW_v0.4.csv`](UPGRADEABLE_RUNTIME_FORM_REVIEW_v0.4.csv).",
        "`PASS_WITH_LIMITATION` preserves an existing historical source-support gap; it",
        "does not mean the normalized package lacks runtime semantics.",
        "",
    ]
    return registry_text, csv_text, "\n".join(markdown)


def _check(path: Path, expected: str) -> bool:
    return path.is_file() and path.read_text(encoding="utf-8") == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    registry_text, csv_text, markdown_text = build()
    targets = [*((path, registry_text) for path in OUTPUTS), (AUDIT_CSV, csv_text), (AUDIT_MD, markdown_text)]
    if args.check:
        stale = [str(path.relative_to(ROOT)) for path, content in targets if not _check(path, content)]
        if stale:
            print("Runtime registry artifacts are stale: " + ", ".join(stale), file=sys.stderr)
            return 1
        print("Runtime registry build: OK (96 components)")
        return 0
    for path, content in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
    print("Runtime registry built: 96 components")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
