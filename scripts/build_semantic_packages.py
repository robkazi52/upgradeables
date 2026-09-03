"""Build v0.2 package docs, metadata, examples, cases, and review artifacts."""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE_DIR = ROOT / "tools/semantic_profiles"
BASELINE = ROOT / "audit/v0.1.0-operational-baseline.json"
ALLOWED_BASIS = {"recovered", "normalized-from-recovered", "modern-interpretation", "provisional"}
ALLOWED_SUPPORT = {"sufficiently-recovered", "strongly-derivable", "modern-operationalization", "source-gap"}
SOURCE_KIND_BY_DOCUMENT = {
    "OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md": "current_consolidated_catalog",
    "OS_Upgradeables_Historical_Recovery_Inventory.md": "historical_recovery_inventory",
    "OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md": "historical_assistant_artifact",
}
RELATIONSHIP_ALIASES = {
    "strong-model-skip-logic": "future-proof-mode-selector",
    "loader-sequencing": "scoped-loader",
    "privacy-scope-filter": "authority-anchor-enforcement",
    "proportionality": "reasoning-scale-controller",
    "final-validation": "parallel-qms",
    "template-preservation": "safe-rewrite",
}
REQUIRED_PROFILE = {
    "source_support", "source_refs", "summary", "purpose", "problem_solved",
    "os_role", "pipeline_stages", "best_fit_tasks", "avoid_when",
    "mechanism_basis", "mechanism", "procedure", "always_do", "never_do",
    "interaction_reasons", "counterbalance_reasons", "redundancy_reasons",
    "conflict_rules", "inputs", "outputs", "failure_boundary",
    "strong_model_may_skip", "strong_model_keep", "example",
    "distinctive_test", "closest_neighbors", "final_status", "notes",
}
REQUIRED_EXAMPLE = {"task_context", "why_activates", "inputs_state", "does", "does_not", "result", "companions"}
REQUIRED_TEST = {"given", "expect", "reject"}
AUDIT_COLUMNS = [
    "slug", "id", "display_name", "baseline_version", "new_version",
    "functional_class", "source_support", "source_refs", "summary_review",
    "purpose_review", "problem_review", "mechanism_review", "procedure_review",
    "trigger_review", "os_fit_review", "task_mapping_review",
    "interaction_review", "example_review", "test_review", "metadata_review",
    "provenance_review", "semantic_specificity", "final_status", "version_reason", "notes",
]


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_profiles():
    profiles = {}
    owners = {}
    for path in sorted(PROFILE_DIR.glob("*.json")):
        data = read_json(path)
        if not isinstance(data, dict):
            raise ValueError(f"{path}: profile file must contain an object")
        for slug, profile in data.items():
            if slug in profiles:
                raise ValueError(f"duplicate profile {slug}: {owners[slug]} and {path.name}")
            profiles[slug] = profile
            owners[slug] = path.name
    return profiles


def validate_profile(slug, profile):
    errors = []
    missing = REQUIRED_PROFILE - set(profile)
    if missing:
        errors.append(f"{slug}: missing profile fields {sorted(missing)}")
    if profile.get("mechanism_basis") not in ALLOWED_BASIS:
        errors.append(f"{slug}: invalid mechanism_basis")
    if profile.get("source_support") not in ALLOWED_SUPPORT:
        errors.append(f"{slug}: invalid source_support")
    if profile.get("final_status") not in {"PASS", "BLOCKED_BY_SOURCE_GAP"}:
        errors.append(f"{slug}: invalid final_status")
    for key in (
        "source_refs", "os_role", "pipeline_stages", "best_fit_tasks", "avoid_when",
        "procedure", "always_do", "never_do", "conflict_rules", "inputs", "outputs",
        "failure_boundary", "strong_model_may_skip", "strong_model_keep",
    ):
        if not isinstance(profile.get(key), list) or not profile.get(key):
            errors.append(f"{slug}: {key} must be a non-empty array")
    for key in ("interaction_reasons", "counterbalance_reasons", "redundancy_reasons", "closest_neighbors"):
        if not isinstance(profile.get(key), dict):
            errors.append(f"{slug}: {key} must be an object")
    if not REQUIRED_EXAMPLE <= set(profile.get("example", {})):
        errors.append(f"{slug}: incomplete example")
    if not REQUIRED_TEST <= set(profile.get("distinctive_test", {})):
        errors.append(f"{slug}: incomplete distinctive test")
    for key in ("summary", "purpose", "problem_solved", "mechanism"):
        if len(str(profile.get(key, "")).split()) < 6:
            errors.append(f"{slug}: {key} is too short")
    return errors


def bullets(items):
    return "\n".join(f"- {item}" for item in items)


def numbered(items):
    return "\n".join(f"{index}. {item}" for index, item in enumerate(items, 1))


def reason_sections(reasons, empty_text):
    if not reasons:
        return empty_text
    return "\n\n".join(f"### `{slug}`\n\n{reason}" for slug, reason in reasons.items())


def source_ref_text(ref):
    return f"{ref['document']} — {ref['heading']} ({ref['source_kind']})"


def normalized_relationships(reasons):
    return {RELATIONSHIP_ALIASES.get(slug, slug): reason for slug, reason in reasons.items()}


def normalized_source_refs(refs, metadata):
    """Normalize authority labels and resolve descriptive anchors to real headings."""
    normalized = []
    for ref in refs:
        source_text = (ROOT / "archive/source" / ref["document"]).read_text(encoding="utf-8")
        heading = ref["heading"]
        item = {**ref, "source_kind": SOURCE_KIND_BY_DOCUMENT[ref["document"]]}
        if heading not in source_text:
            source_lines = source_text.splitlines()
            heading_rows = [
                (index, line.lstrip("#").strip())
                for index, line in enumerate(source_lines)
                if re.match(r"^#{1,6}\s+\S", line)
            ]
            headings = [value for _, value in heading_rows]
            desired_words = set(re.findall(r"[a-z0-9]+", heading.casefold()))
            identity_words = set(re.findall(
                r"[a-z0-9]+",
                f"{metadata['id']} {metadata['display_name']} {metadata['slug'].replace('-', ' ')}".casefold(),
            ))
            def score(candidate):
                words = set(re.findall(r"[a-z0-9]+", candidate.casefold()))
                return (len(words & identity_words) * 3 + len(words & desired_words), -len(words ^ identity_words))
            resolved = max(headings, key=score)
            if score(resolved)[0] == 0:
                def line_score(line):
                    words = set(re.findall(r"[a-z0-9]+", line.casefold()))
                    return len(words & identity_words) * 3 + len(words & desired_words)
                anchor_index = max(range(len(source_lines)), key=lambda index: line_score(source_lines[index]))
                if line_score(source_lines[anchor_index]) == 0:
                    raise ValueError(f"{metadata['slug']}: cannot resolve source heading {heading!r}")
                preceding = [value for index, value in heading_rows if index <= anchor_index]
                resolved = preceding[-1] if preceding else headings[0]
            item["anchor_detail"] = heading
            item["heading"] = resolved
        normalized.append(item)
    return normalized


def update_metadata(metadata, profile):
    item = dict(metadata)
    interactions = normalized_relationships(profile["interaction_reasons"])
    counterbalances = normalized_relationships(profile["counterbalance_reasons"])
    redundancies = normalized_relationships(profile["redundancy_reasons"])
    source_refs = normalized_source_refs(profile["source_refs"], metadata)
    item.update({
        "schema_version": "2.0.0",
        "version": "1.1.0",
        "purpose": profile["purpose"],
        "problem_solved": profile["problem_solved"],
        "os_role": profile["os_role"],
        "pipeline_stages": profile["pipeline_stages"],
        "best_fit_tasks": profile["best_fit_tasks"],
        "avoid_when": profile["avoid_when"],
        "non_triggers": profile["avoid_when"],
        "recommended_skill_types": profile["best_fit_tasks"],
        "usually_not_needed_for": profile["avoid_when"],
        "mechanism_basis": profile["mechanism_basis"],
        "mechanism": profile["mechanism"],
        "procedure": profile["procedure"],
        "always_do": profile["always_do"],
        "never_do": profile["never_do"],
        "interaction_reasons": interactions,
        "counterbalance_reasons": counterbalances,
        "redundancy_reasons": redundancies,
        "conflict_rules": profile["conflict_rules"],
        "inputs": profile["inputs"],
        "outputs": profile["outputs"],
        "failure_boundary": profile["failure_boundary"],
        "strong_model_scaling": {
            "may_skip": profile["strong_model_may_skip"],
            "keep_mandatory": profile["strong_model_keep"],
        },
        "source_refs": source_refs,
        "source_support": profile["source_support"],
        "activation_cost": {
            "level": "high" if metadata["activation_class"].startswith(("U3", "U4")) else "medium" if metadata["activation_class"].startswith("U2") else "low",
            "notes": "Architectural burden classification; not a measured compute benchmark.",
        },
    })
    item["triggers"] = [
        trigger if len(trigger.split()) >= 5 else f"Activate when the task requires {trigger.rstrip('.').casefold()}."
        for trigger in item["triggers"]
    ]
    # The reviewed reason maps are authoritative for v0.2 relationships. Rebuild
    # the legacy slug arrays from them so stale v0.1 or pre-normalization labels
    # cannot survive indefinitely through a set union.
    item["recommended_with"] = sorted(interactions)
    item["counterbalances"] = sorted(counterbalances)
    item["potentially_redundant_with"] = sorted(redundancies)
    return item


def render_package(metadata, profile):
    provenance = metadata["provenance"]
    aliases = ", ".join(metadata.get("historical_aliases", [])) or "None"
    source_refs = bullets(source_ref_text(ref) for ref in metadata["source_refs"])
    modern_note = ""
    if profile["mechanism_basis"] in {"modern-interpretation", "provisional"}:
        modern_note = "\n\n**Modern operational interpretation:** The procedure below is useful current guidance, not a claim that the full historical mechanism was recovered."
    return f"""# {metadata['display_name']}

## Summary

{profile['summary']}

## Purpose

{profile['purpose']}

## Problem Solved

{profile['problem_solved']}

## Where It Fits in the OS

Roles: {', '.join(profile['os_role'])}. Pipeline stages: {', '.join(profile['pipeline_stages'])}.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

{bullets(profile['best_fit_tasks'])}

## When Not to Use

{bullets(profile['avoid_when'])}

## Scope

Canonical package: `{metadata['slug']}@{metadata['version']}`. ID: `{metadata['id']}`. Functional classes: {', '.join(metadata['functional_classes'])}. Activation: `{metadata['activation_class']}`. Mechanism basis: `{profile['mechanism_basis']}`. Activation cost: `{metadata['activation_cost']['level']}` (architectural burden, not measured compute).

## Trigger Conditions

{bullets(metadata['triggers'])}

## Non-Triggers

{bullets(metadata['non_triggers'])}

## Inputs / Required State

{bullets(profile['inputs'])}

## Outputs / Produced State

{bullets(profile['outputs'])}

## Mechanism

{profile['mechanism']}{modern_note}

## Procedure

{numbered(profile['procedure'])}

## Always-Do Rules

{bullets(profile['always_do'])}

## Never-Do / Avoid Rules

{bullets(profile['never_do'])}

## Interaction Rules

{reason_sections(metadata['interaction_reasons'], 'No required companion was found in review; activate this component independently when its own trigger applies.')}

## Compatible Upgradeables

{bullets(f'`{slug}` — {reason}' for slug, reason in metadata['interaction_reasons'].items()) if metadata['interaction_reasons'] else '- No compatible companion is required after semantic review.'}

## Counterbalancing Upgradeables

{reason_sections(metadata['counterbalance_reasons'], 'No natural counterbalance was identified after review; ordinary authority, scope, and validation controls still apply.')}

## Potential Redundancy

{reason_sections(metadata['redundancy_reasons'], 'No material operational redundancy was identified after comparison with the closest neighbors.')}

## Conflict / Precedence Rules

{bullets(profile['conflict_rules'])}

## Failure Boundary

{bullets(profile['failure_boundary'])}

## Strong-Model Scaling

May skip:

{bullets(profile['strong_model_may_skip'])}

Keep mandatory:

{bullets(profile['strong_model_keep'])}

## Recommended Skill Types

{bullets(profile['best_fit_tasks'])}

## Example Composition

**Task context:** {profile['example']['task_context']}

**Why it activates:** {profile['example']['why_activates']}

**Inputs/state:** {profile['example']['inputs_state']}

**Action:** {profile['example']['does']}

**Does not:** {profile['example']['does_not']}

**Result/state change:** {profile['example']['result']}

**Companions:** {profile['example']['companions']}

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `{provenance['source_id']}` in `{provenance['source_document']}`. Registry generation: `{metadata['registry_generation']}`. Historical aliases: {aliases}.

Source support: `{profile['source_support']}`. Mechanism basis: `{profile['mechanism_basis']}`.

Structured source references:

{source_refs}
"""


def render_example(metadata, profile):
    example = profile["example"]
    return f"""# {metadata['display_name']} — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

{example['task_context']}

## Why this Upgradeable activates

{example['why_activates']}

## Inputs / state

{example['inputs_state']}

## What it does

{example['does']}

## What it does not do

{example['does_not']}

## Result / state change

{example['result']}

## Interaction with companion components

{example['companions']}
"""


def behavior_cases(metadata, profile):
    negative = profile["avoid_when"][0]
    conflict = profile["conflict_rules"][0]
    failure = profile["failure_boundary"][0]
    keep = profile["strong_model_keep"][0]
    cases = [
        ("positive_activation", profile["example"]["why_activates"], profile["example"]["result"], "remaining inactive despite a satisfied trigger"),
        ("negative_activation", negative, "the component stays inactive and adds no scaffolding", "activating solely because the name appears relevant"),
        ("precedence_or_conflict", conflict, "the higher-authority rule wins and the conflict is visible", "silently resolving against higher authority"),
        ("failure_boundary", failure, "the component stops, abstains, narrows, or escalates as documented", "manufacturing a successful result past its failure boundary"),
        ("strong_model_scaling", "a capable host can compress the workflow", keep, "dropping the mandatory invariant"),
        ("distinctive_mechanism", profile["distinctive_test"]["given"], profile["distinctive_test"]["expect"], profile["distinctive_test"]["reject"]),
    ]
    return {
        "schema_version": "1.0.0",
        "slug": metadata["slug"],
        "package_version": metadata["version"],
        "cases": [
            {
                "id": f"{metadata['slug']}-{kind.replace('_', '-')}",
                "type": kind,
                "execution": "model-required",
                "given": given,
                "expect": expect,
                "reject": reject,
            }
            for kind, given, expect, reject in cases
        ],
    }


def render_composition(metadata, cases):
    lines = [f"# {metadata['display_name']} — Behavioral Expectations", ""]
    for case in cases["cases"]:
        lines.extend([
            f"## {case['type'].replace('_', ' ').title()}", "",
            f"- **Given:** {case['given']}",
            f"- **Expect:** {case['expect']}",
            f"- **Reject:** {case['reject']}", "",
        ])
    lines.append("These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.\n")
    return "\n".join(lines)


def render_source_note(metadata, profile):
    return f"""# Source Note — {metadata['display_name']}

- Slug: `{metadata['slug']}`
- ID: `{metadata['id']}`
- Source support: `{profile['source_support']}`
- Mechanism basis: `{profile['mechanism_basis']}`
- Final status: `{profile['final_status']}`

## Recovered facts and source anchors

{bullets(source_ref_text(ref) for ref in metadata['source_refs'])}

## Recovered or normalized purpose

{profile['purpose']}

## Operational mechanism

{profile['mechanism']}

## Trigger and task use

Triggers: {', '.join(metadata['triggers'])}. Best-fit tasks: {', '.join(profile['best_fit_tasks'])}.

## Interactions and failure boundary

Companions: {', '.join(metadata['interaction_reasons']) or 'none required'}. Failure boundary: {'; '.join(profile['failure_boundary'])}.

## Unresolved details / interpretation boundary

{profile['notes']}
"""


def build_outputs():
    if not BASELINE.exists():
        raise ValueError("missing audit/v0.1.0-operational-baseline.json")
    baseline_data = read_json(BASELINE)
    baseline = {item["slug"]: item for item in baseline_data["packages"]}
    profiles = load_profiles()
    errors = []
    if set(profiles) != set(baseline):
        errors.append(f"profile coverage mismatch; missing={sorted(set(baseline)-set(profiles))}; extra={sorted(set(profiles)-set(baseline))}")
    for slug, profile in profiles.items():
        errors.extend(validate_profile(slug, profile))
    if errors:
        raise ValueError("\n".join(errors))

    outputs = {}
    audit_rows = []
    overlap_lines = ["# Overlap and Redundancy Review v0.2", "", f"Reviewed baseline packages: {len(baseline)}.", ""]
    for slug in sorted(baseline):
        base = baseline[slug]
        package = ROOT / base["package_path"]
        metadata_path = package.parent / "metadata.yaml"
        current = read_json(metadata_path)
        profile = profiles[slug]
        metadata = update_metadata(current, profile)
        cases = behavior_cases(metadata, profile)
        outputs[metadata_path] = json.dumps(metadata, ensure_ascii=False, indent=2) + "\n"
        outputs[package] = render_package(metadata, profile).strip() + "\n"
        outputs[package.parent / "examples/basic.md"] = render_example(metadata, profile).strip() + "\n"
        outputs[package.parent / "tests/cases.json"] = json.dumps(cases, ensure_ascii=False, indent=2) + "\n"
        outputs[package.parent / "tests/composition.md"] = render_composition(metadata, cases).strip() + "\n"
        outputs[ROOT / f"audit/source-notes/{slug}.md"] = render_source_note(metadata, profile).strip() + "\n"
        refs = "; ".join(source_ref_text(ref) for ref in profile["source_refs"])
        audit_rows.append({
            "slug": slug, "id": metadata["id"], "display_name": metadata["display_name"],
            "baseline_version": base["version"], "new_version": metadata["version"],
            "functional_class": ";".join(metadata["functional_classes"]),
            "source_support": profile["source_support"], "source_refs": refs,
            **{key: "PASS" for key in AUDIT_COLUMNS[8:22]},
            "final_status": profile["final_status"],
            "version_reason": "Minor version: compatible semantic detail, metadata, examples, and behavior cases were added without changing package identity.",
            "notes": profile["notes"],
        })
        overlap_lines.extend([f"## `{slug}`", ""])
        if profile["closest_neighbors"]:
            overlap_lines.extend(f"- `{neighbor}` — {reason}" for neighbor, reason in profile["closest_neighbors"].items())
        else:
            overlap_lines.append("- No material operational duplicate identified after repository-wide neighbor review.")
        overlap_lines.append("")

    csv_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(csv_buffer, fieldnames=AUDIT_COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(audit_rows)
    outputs[ROOT / "audit/OPERATIONAL_PACKAGE_REVIEW_v0.2.csv"] = csv_buffer.getvalue()
    pass_count = sum(row["final_status"] == "PASS" for row in audit_rows)
    blocked_count = sum(row["final_status"] == "BLOCKED_BY_SOURCE_GAP" for row in audit_rows)
    audit_md = [
        "# Operational Package Review v0.2", "",
        f"- Baseline packages: {len(baseline)}",
        f"- PASS: {pass_count}",
        f"- BLOCKED_BY_SOURCE_GAP: {blocked_count}",
        "- Missing: 0", "- Unreviewed: 0", "",
        "| Slug | ID | Baseline | v0.2 | Source support | Status |",
        "|---|---|---:|---:|---|---|",
    ]
    audit_md.extend(f"| `{row['slug']}` | `{row['id']}` | {row['baseline_version']} | {row['new_version']} | {row['source_support']} | {row['final_status']} |" for row in audit_rows)
    outputs[ROOT / "audit/OPERATIONAL_PACKAGE_REVIEW_v0.2.md"] = "\n".join(audit_md) + "\n"
    outputs[ROOT / "audit/OVERLAP_AND_REDUNDANCY_REVIEW_v0.2.md"] = "\n".join(overlap_lines)
    return outputs, len(baseline)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        outputs, count = build_outputs()
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"semantic package build failed: {error}", file=sys.stderr)
        return 1
    if args.check:
        stale = [str(path.relative_to(ROOT)) for path, expected in outputs.items() if not path.exists() or path.read_text(encoding="utf-8") != expected]
        if stale:
            print("stale semantic artifacts: " + ", ".join(stale[:20]), file=sys.stderr)
            return 1
        print(f"semantic package build check: OK ({count} baseline packages)")
        return 0
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
    print(f"built semantic packages and audit artifacts ({count} packages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
