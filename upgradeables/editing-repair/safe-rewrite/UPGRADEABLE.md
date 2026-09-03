# Safe Rewrite Logic

## Summary

Changes only requested presentation dimensions while preserving locked meaning, facts, constraints, names, numbers, dates, quotes, and citations.

## Purpose

Make paraphrase, polish, tone, or formatting safe by treating content atoms as invariants rather than suggestions.

## Problem Solved

Fluent rewriting can introduce factual drift, altered modality, citation mismatch, or lost requirements even when the request is purely stylistic.

## Where It Fits in the OS

Roles: editing guard, semantic preservation layer. Pipeline stages: rewrite planning, controlled transformation, atom-level comparison.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- paraphrasing
- tone adjustment
- format conversion
- clarity polishing
- audience adaptation

## When Not to Use

- the user asks to change substantive meaning
- the source is internally contradictory and needs adjudication
- global structure is broken

## Scope

Canonical package: `safe-rewrite@1.1.0`. ID: `T1-10`. Functional classes: editing-repair, truth-grounding. Activation: `U0-foundational`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- paraphrasing, polishing, or format conversion

## Non-Triggers

- the user asks to change substantive meaning
- the source is internally contradictory and needs adjudication
- global structure is broken

## Inputs / Required State

- source artifact
- authorized change dimensions
- locked atom ledger
- target style or format

## Outputs / Produced State

- rewritten artifact
- atom-preservation check
- reported transformation conflicts

## Mechanism

Extract a before-state ledger of factual and constraint atoms, mark the dimensions authorized to change, perform the rewrite only along those dimensions, then compare names, numbers, dates, quotes, citations, modality, requirements, and causal claims. Any atom difference not explicitly authorized is reverted or surfaced for approval.

## Procedure

1. Identify authorized change dimensions such as tone, length, format, or reading level.
2. Extract locked atoms: claims, entities, numbers, dates, quotations, citations, requirements, negations, and uncertainty markers.
3. Rewrite without adding evidence or changing the locked atoms.
4. Diff the rewritten artifact against the atom ledger and inspect citation-to-claim fit.
5. Restore unauthorized changes and report any requested transformation that cannot preserve meaning.

## Always-Do Rules

- separate semantic atoms from surface form
- preserve modality and uncertainty
- recheck citations against the rewritten claims

## Never-Do / Avoid Rules

- add plausible facts for smoothness
- alter numbers or named entities silently
- turn qualified language into certainty
- move a citation so it appears to support a different claim

## Interaction Rules

### `micro-repair`

Micro-Repair bounds the rewritten region when only one passage is defective.

### `citation-fidelity`

Citation Fidelity performs the source-to-claim validation required after wording changes.

### `style-alignment`

Style Alignment specifies one authorized surface dimension while Safe Rewrite protects semantics.

## Compatible Upgradeables

- `micro-repair` — Micro-Repair bounds the rewritten region when only one passage is defective.
- `citation-fidelity` — Citation Fidelity performs the source-to-claim validation required after wording changes.
- `style-alignment` — Style Alignment specifies one authorized surface dimension while Safe Rewrite protects semantics.

## Counterbalancing Upgradeables

### `regenerative-rewrite`

Regenerative Rewrite is needed when preservation of the old structure prevents a coherent result.

## Potential Redundancy

### `style-alignment`

Style Alignment selects the target voice; Safe Rewrite is the preservation guard across any transformation dimension.

### `crispr-edit`

CRISPR changes a named semantic rule while preserving other invariants; Safe Rewrite generally forbids semantic change and transforms expression.

## Conflict / Precedence Rules

- Truth and locked constraints outrank requested style.
- If shortening would remove a required qualification, keep the qualification or report the conflict.
- Exact quotations remain exact unless the user authorizes conversion to paraphrase.

## Failure Boundary

- semantic drift
- citation drift
- lost negation or uncertainty
- unrequested content addition
- meaning change hidden as polish

## Strong-Model Scaling

May skip:

- printing the full atom ledger for a tiny rewrite

Keep mandatory:

- internal atom extraction
- authorized-dimension discipline
- post-rewrite names/numbers/dates/quotes/citations check

## Recommended Skill Types

- paraphrasing
- tone adjustment
- format conversion
- clarity polishing
- audience adaptation

## Example Composition

**Task context:** Shorten a technical update for executives.

**Why it activates:** Length and jargon may change, but findings and uncertainty must not.

**Inputs/state:** The update contains three metrics, one date, two caveats, and a citation.

**Action:** Condenses explanations, preserves all metrics and caveats, and confirms the citation still supports the adjacent claim.

**Does not:** Round the numbers, drop uncertainty, or add a business implication absent from the source.

**Result/state change:** A shorter update with unchanged factual atoms.

**Companions:** ['style-alignment', 'citation-fidelity']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T1-10` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T1-10. Safe Rewrite Logic (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 5. January 5, 2026 — training/scaffolding Upgradeables snapshot (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 17. VERBATIM-COPY / FIDELITY WORKFLOW — EXAMPLE OF UPGRADEABLE COMPOSITION (historical_assistant_artifact)
