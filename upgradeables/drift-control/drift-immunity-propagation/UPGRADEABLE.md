# Drift Immunity Propagation

## Summary

Carry protected invariants and their validation rules through every derivative artifact and downstream component so later transformations cannot silently weaken them.

## Purpose

Preserve established drift resistance across pipelines rather than only at the original source boundary.

## Problem Solved

A fact may be locked in the first stage yet lose its protection when summarized, projected, handed off, or transformed again.

## Where It Fits in the OS

Roles: invariant propagation, derivation lineage, downstream validation. Pipeline stages: artifact derivation, state projection, agent handoff, final aggregation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-stage generation
- agent pipelines
- source-to-summary-to-decision workflows
- format conversion chains

## When Not to Use

- no downstream artifact derives from protected material
- protection metadata cannot accompany data and downstream validation is impossible
- the claimed invariant was never verified

## Scope

Canonical package: `drift-immunity-propagation@1.1.0`. ID: `T4-14`. Functional classes: drift-control, state. Activation: `U2-specialized`. Mechanism basis: `normalized-from-recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- many downstream modules consume locked decisions

## Non-Triggers

- no downstream artifact derives from protected material
- protection metadata cannot accompany data and downstream validation is impossible
- the claimed invariant was never verified

## Inputs / Required State

- verified invariant records
- source provenance
- derivation graph
- consumer contracts
- validation predicates

## Outputs / Produced State

- invariant-bearing derivatives
- lineage graph
- boundary validation results
- explicit rejection record

## Mechanism

Represent each verified invariant with an identifier, source/provenance, scope, permitted transformations, and validation predicate. When producing a derived artifact or state projection, copy the applicable invariant contract and lineage pointer, require the receiver to acknowledge it, and test the derivative before it can become an upstream source for another stage.

## Procedure

1. Identify verified invariants and assign stable identifiers.
2. Define the derivation scope and validation predicate for each.
3. Attach applicable invariant contracts to every downstream projection or artifact.
4. Require receiving components to preserve or explicitly reject unsupported contracts.
5. Validate each derivative before further propagation.
6. Trace final claims back through lineage to the original protected source.

## Always-Do Rules

- propagate provenance with protection
- scope invariants to applicable fields
- validate at every derivative boundary
- make rejection explicit

## Never-Do / Avoid Rules

- propagate an unverified claim as immune
- copy labels without validation predicates
- assume protection survives a lossy transform automatically

## Interaction Rules

### `zero-drift-zones`

Supplies the invariants whose immunity must travel downstream.

### `structured-state-projection`

Carries the invariant contract with the filtered state view.

### `drift-suppression`

Tests and repairs downstream deviations.

## Compatible Upgradeables

- `zero-drift-zones` — Supplies the invariants whose immunity must travel downstream.
- `structured-state-projection` — Carries the invariant contract with the filtered state view.
- `drift-suppression` — Tests and repairs downstream deviations.

## Counterbalancing Upgradeables

### `controlled-drift-corridors`

Limits propagation to fixed dimensions while allowing explicit change elsewhere.

### `scoped-loader`

Loads only applicable invariant contracts, avoiding global constraint pollution.

## Potential Redundancy

### `working-memory-lock-in`

WM Lock protects current attention; propagation protects lineage across component boundaries.

### `zero-drift-zones`

Zero-drift defines immutability; propagation ensures that definition survives derivation.

## Conflict / Precedence Rules

- Original verified source and higher-authority constraints outrank downstream paraphrases.
- If two inherited invariant contracts conflict, stop derivation and resolve lineage/authority before merging.

## Failure Boundary

- Do not label a derivative immune when its invariant cannot be tested.
- Stop propagation across a component that cannot preserve required provenance or semantics.

## Strong-Model Scaling

May skip:

- verbose contract restatement inside a single atomic transformation
- manual acknowledgements where typed interfaces enforce them

Keep mandatory:

- stable invariant identity
- lineage
- boundary tests
- no immunity for unverified claims

## Recommended Skill Types

- multi-stage generation
- agent pipelines
- source-to-summary-to-decision workflows
- format conversion chains

## Example Composition

**Task context:** Cited financial figures move from extraction to analysis to an executive slide.

**Why it activates:** Each stage could round, relabel, or detach the figures from their period.

**Inputs/state:** Verified figure IDs, source cells, period/currency constraints, and equality/tolerance tests.

**Action:** Carries those contracts into analysis and slide projections and validates each derivative.

**Does not:** It does not propagate a confidence label without the source period or allow silent unit changes.

**Result/state change:** Final figures retain source identity and protected semantics through the pipeline.

**Companions:** ['zero-drift-zones', 'structured-state-projection', 'drift-suppression']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-14` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: DIP.

Source support: `strongly-derivable`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — Drift Immunity Propagation (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — ECL / Drift Sink (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — Zero-drift (historical_assistant_artifact)
