# Controlled Drift Corridors

## Summary

Define explicit transformation boundaries for a task region so useful variation is allowed only along named dimensions and within testable limits.

## Purpose

Enable adaptation, compression, or creativity without surrendering semantic control.

## Problem Solved

A binary exact-copy versus free-rewrite choice is too crude for work where wording may change but claims, obligations, or structure have different tolerances.

## Where It Fits in the OS

Roles: bounded transformation policy, regional drift control, acceptance envelope. Pipeline stages: task decomposition, transformation planning, generation, semantic validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- document rewriting
- cross-format conversion
- summarization
- creative work with fixed constraints

## When Not to Use

- all content is zero-drift
- allowed dimensions cannot be tested
- the user expects unconstrained ideation

## Scope

Canonical package: `controlled-drift-corridors@1.1.0`. ID: `T3-02`. Functional classes: drift-control, truth-grounding. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- synthesis or creativity must coexist with fidelity

## Non-Triggers

- all content is zero-drift
- allowed dimensions cannot be tested
- the user expects unconstrained ideation

## Inputs / Required State

- source regions
- allowed-change dimensions
- locked invariants
- semantic tests
- rollback threshold

## Outputs / Produced State

- region-specific corridor map
- validated transformed regions
- exception and rollback record

## Mechanism

Partition the artifact into regions or claim types and assign each a corridor specifying fixed invariants, allowed dimensions of change, maximum semantic distance, evidence requirements, and rollback trigger. Transform only after the corridor is explicit, then compare output to the source and tighten or revert any region outside bounds.

## Procedure

1. Segment the task into regions with materially different tolerance.
2. For each region, list invariants and allowed changes such as tone, length, order, or abstraction.
3. Set validation metrics or review questions and a rollback threshold.
4. Transform one region inside its corridor.
5. Compare claims, obligations, entities, and required structure to source.
6. Accept, tighten, or revert; record any authorized exception.

## Always-Do Rules

- make drift opt-in and dimension-specific
- protect source meaning
- test each region
- define rollback

## Never-Do / Avoid Rules

- treat a corridor as permission for new unsupported claims
- assign one width to heterogeneous content
- expand the corridor after a failure without authority

## Interaction Rules

### `zero-drift-zones`

Marks regions whose corridor width is zero.

### `drift-spectra-scaling`

Provides the map used to choose different corridor widths.

### `drift-suppression`

Detects excursions and restores content to the corridor.

## Compatible Upgradeables

- `zero-drift-zones` — Marks regions whose corridor width is zero.
- `drift-spectra-scaling` — Provides the map used to choose different corridor widths.
- `drift-suppression` — Detects excursions and restores content to the corridor.

## Counterbalancing Upgradeables

### `mode-lock-in`

Keeps the overall transformation regime stable while bounded local variation occurs.

### `clarification-gateway`

Resolves unspecified transformation freedoms before assigning a corridor.

## Potential Redundancy

### `domain-normalized-drift`

Domain normalization supplies a default corridor; the task-specific corridor should override it explicitly rather than layering two bounds.

### `compute-adaptive-drift`

Compute adaptation changes enforcement process, not the allowed semantic boundary.

## Conflict / Precedence Rules

- Higher-authority task constraints and zero-drift fields override corridor permissions.
- If validation signals disagree, apply the narrowest supported corridor or request review.

## Failure Boundary

- Stop transformation when invariants cannot be measured or recovered.
- Revert regions that cross the boundary instead of rationalizing post hoc.

## Strong-Model Scaling

May skip:

- numeric corridor scoring when qualitative tests are decisive
- per-sentence checks in a low-risk uniform region

Keep mandatory:

- explicit allowed dimensions
- locked invariants
- region-specific validation
- rollback boundary

## Recommended Skill Types

- document rewriting
- cross-format conversion
- summarization
- creative work with fixed constraints

## Example Composition

**Task context:** Turn a technical incident report into an executive brief.

**Why it activates:** Narrative order and length may change, but dates, causal uncertainty, and remediation commitments must not.

**Inputs/state:** Source report, zero-drift facts, tone/length permissions, and claim-level tests.

**Action:** Assigns a wider corridor to prose compression and zero/narrow corridors to dates, causal claims, and commitments.

**Does not:** It does not make causality sound certain for fluency.

**Result/state change:** A shorter readable brief whose protected meanings remain intact.

**Companions:** ['zero-drift-zones', 'drift-suppression', 'drift-spectra-scaling']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-02` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — Controlled Drift Corridors (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — ECL / Drift Sink (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.3 Drift widths (historical_assistant_artifact)
