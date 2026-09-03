# Counterfactual Silence Scaffold

## Summary

A modern factual-mode output guard built from an exactly recovered name: when hypothetical reasoning is not authorized, it removes newly introduced what-if premises and imagined outcomes from the candidate output.

## Purpose

Protect factual extraction and reporting tasks from unsolicited counterfactual elaboration.

## Problem Solved

Prevents plausible alternate scenarios from filling missing evidence or distracting from a factual-only deliverable.

## Where It Fits in the OS

Roles: factual-mode-guard, output-filter. Pipeline stages: task-framing, draft-validation, pre-output-verification.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- record extraction
- source-faithful summarization
- incident reporting
- citation-bound authoring

## When Not to Use

- the task explicitly requests scenarios, hypotheses, or counterfactual analysis
- creative generation is the primary authorized mode

## Scope

Canonical package: `counterfactual-silence-scaffold@1.1.0`. ID: `JAN26-06`. Functional classes: truth-grounding, output. Activation: `U2-specialized`. Mechanism basis: `modern-interpretation`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- factual output could be contaminated by hypothetical content

## Non-Triggers

- the task explicitly requests scenarios, hypotheses, or counterfactual analysis
- creative generation is the primary authorized mode

## Inputs / Required State

- locked factual-only task mode
- source boundary
- candidate output

## Outputs / Produced State

- factual-only candidate
- list of quarantined speculative statements
- mode-conflict status

## Mechanism

After a factual-only mode is locked, inspect the candidate for propositions introduced through if, might-have, imagined, alternative-history, or unstated causal premises. Remove those propositions unless they are explicitly reported as source content; preserve ordinary uncertainty statements and supported inference rather than suppressing all modal language.

**Modern operational interpretation:** The procedure below is useful current guidance, not a claim that the full historical mechanism was recovered.

## Procedure

1. Confirm that the task contract excludes hypothetical reasoning.
2. Identify candidate statements that introduce a non-source counterfactual premise or imagined outcome.
3. Distinguish those statements from source-reported hypotheticals and honest uncertainty.
4. Delete or quarantine unauthorized counterfactual additions.
5. Recheck that the factual answer remains complete and does not fill gaps by implication.

## Always-Do Rules

- Tie activation to an explicit factual-only boundary.
- Preserve source-authored hypothetical statements as attributed source content.
- Preserve uncertainty labels that accurately describe missing evidence.

## Never-Do / Avoid Rules

- Suppress a counterfactual the user explicitly requested.
- Treat every use of could or may as contamination.
- Replace removed speculation with a different unsupported claim.

## Interaction Rules

### `counterfactual-integrity`

Integrity handles explicitly authorized hypothetical branches; silence is the stricter no-branch mode.

### `mode-lock-in`

Provides the factual-only task mode that activates this filter.

## Compatible Upgradeables

- `counterfactual-integrity` — Integrity handles explicitly authorized hypothetical branches; silence is the stricter no-branch mode.
- `mode-lock-in` — Provides the factual-only task mode that activates this filter.

## Counterbalancing Upgradeables

### `controlled-drift-corridors`

Where bounded exploration is authorized, controlled drift prevents silence from over-constraining useful reasoning.

## Potential Redundancy

### `counterfactual-integrity`

Both prevent fact/hypothesis leakage, but silence excludes unauthorized branches while integrity preserves authorized ones with labels.

## Conflict / Precedence Rules

- An explicit user request for counterfactual analysis deactivates this scaffold and activates counterfactual integrity instead.
- Source fidelity outranks a blanket silence rule when the source itself discusses a hypothetical.

## Failure Boundary

- If factual and counterfactual propositions cannot be distinguished reliably, request review rather than deleting uncertain content wholesale.

## Strong-Model Scaling

May skip:

- explicit lexical cue scanning when semantic mode separation is already reliable

Keep mandatory:

- unauthorized hypothetical premises must not enter factual output

## Recommended Skill Types

- communication and content generation
- document and code transformation
- high-stakes evidence work
- source-grounded research

## Example Composition

**Task context:** Summarize an incident report that does not identify a cause.

**Why it activates:** The output must remain factual and the missing cause invites speculation.

**Inputs/state:** Incident chronology with no causal finding and a factual-only output contract.

**Action:** Reports the chronology and marks cause as undetermined.

**Does not:** Add what might have happened if a different operator acted.

**Result/state change:** A factual summary with an explicit evidence gap.

**Companions:** ['mode-lock-in', 'grounding-no-invention']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `JAN26-06` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `training-scaffolding-2026-01-05`. Historical aliases: None.

Source support: `source-gap`. Mechanism basis: `modern-interpretation`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 5. January 5, 2026 — training/scaffolding Upgradeables snapshot (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 6.2 T3 structured reasoning-state representation (historical_assistant_artifact)
