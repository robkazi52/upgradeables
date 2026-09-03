# Two Truths + Corridor

## Summary

A composite synthesis control that locks two independent factual anchors and permits only a declared width of interpretation between or around them.

## Purpose

Enable useful synthesis without losing redundant factual grounding.

## Problem Solved

Prevents a synthesis from either parroting two sources without integration or drifting beyond what either anchor can support.

## Where It Fits in the OS

Roles: grounded-synthesis-controller, drift-boundary. Pipeline stages: pre-synthesis, synthesis, post-synthesis-validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- comparative research
- evidence-grounded authoring
- policy synthesis
- explanatory integration of two sources

## When Not to Use

- only one defensible anchor exists
- the task requires exact extraction with zero interpretive drift
- the task permits unconstrained creative ideation

## Scope

Canonical package: `two-truths-and-corridor@1.1.0`. ID: `T3-08`. Functional classes: truth-grounding, drift-control. Activation: `U2-specialized`. Mechanism basis: `normalized-from-recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- source-grounded synthesis permits bounded interpretation

## Non-Triggers

- only one defensible anchor exists
- the task requires exact extraction with zero interpretive drift
- the task permits unconstrained creative ideation

## Inputs / Required State

- two independent anchors
- locked truth atoms
- declared corridor width
- synthesis objective

## Outputs / Produced State

- bounded source-traceable synthesis
- corridor-breach report
- unresolved anchor conflict

## Mechanism

Verify two independent anchors, declare which atoms in them are fixed, and set the synthesis corridor to zero, micro, or bounded exploratory drift. Generate connecting interpretation only inside that corridor, then check every synthesized claim against at least one anchor and the permitted transformation width.

## Procedure

1. Select and verify two independent anchors.
2. Extract the fixed facts and any material disagreement.
3. Declare the allowed synthesis corridor and prohibited transformations.
4. Create the synthesis while keeping each connection traceable.
5. Audit the result for unsupported bridging claims or altered anchor meaning.
6. Narrow or reject the synthesis when the corridor is exceeded.

## Always-Do Rules

- Verify both anchors before synthesis.
- Declare corridor width before writing.
- Keep disagreements visible rather than manufacturing harmony.

## Never-Do / Avoid Rules

- Use a corridor to introduce a third unsupported truth.
- Paraphrase exact locked atoms when zero drift applies.
- Treat two dependent sources as independent anchors.

## Interaction Rules

### `truth-redundancy`

Supplies and checks the two independent anchors.

### `controlled-drift-corridors`

Defines the permitted transformation width.

### `multi-truth-gating`

Handles material disagreement between the anchors before synthesis is committed.

## Compatible Upgradeables

- `truth-redundancy` — Supplies and checks the two independent anchors.
- `controlled-drift-corridors` — Defines the permitted transformation width.
- `multi-truth-gating` — Handles material disagreement between the anchors before synthesis is committed.

## Counterbalancing Upgradeables

### `grounding-no-invention`

Constrains corridor-generated prose to supported interpretation.

## Potential Redundancy

### `truth-redundancy`

Truth Redundancy stops after creating an anchor pair; this composite additionally governs the synthesis space between them.

## Conflict / Precedence Rules

- Zero-drift atoms override a wider surrounding synthesis corridor.
- If the anchors materially conflict, resolve or expose the conflict before generating a unified narrative.

## Failure Boundary

- If either anchor is unverified or the synthesis requires claims outside the declared corridor, do not certify the synthesis.

## Strong-Model Scaling

May skip:

- verbose mapping for simple one-sentence integration

Keep mandatory:

- two verified anchors and the declared transformation boundary

## Recommended Skill Types

- document and code transformation
- high-stakes evidence work
- long-context workflows
- source-grounded research

## Example Composition

**Task context:** Two studies support complementary mechanisms and the writer must explain their relationship.

**Why it activates:** The task needs bounded interpretation across two sources.

**Inputs/state:** Verified findings from each study and a micro-drift corridor allowing connective explanation.

**Action:** Links compatible findings and labels a remaining disagreement.

**Does not:** Invent a causal mechanism neither study supports.

**Result/state change:** An integrated but source-bounded paragraph.

**Companions:** ['truth-redundancy', 'controlled-drift-corridors', 'multi-truth-gating']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-08` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `strongly-derivable`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 8. Tier-3 / Paper-Author alignment family recovered from late-November work (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.3 Drift widths (historical_assistant_artifact)
