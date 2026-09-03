# Drift-Spectra Scaling

## Summary

Map heterogeneous task regions onto an ordered spectrum of semantic drift tolerance instead of treating fidelity as a binary setting.

## Purpose

Allocate strictness where meaning is fragile and flexibility where variation is valuable.

## Problem Solved

Artifacts mix identifiers, facts, reasoning, organization, explanation, and style, each requiring a different permissible degree of change.

## Where It Fits in the OS

Roles: drift classification, fidelity planning, validation allocation. Pipeline stages: content decomposition, risk classification, corridor assignment, review prioritization.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- mixed-content rewriting
- summaries
- format migrations
- multi-stage synthesis

## When Not to Use

- every element has the same explicit tolerance
- classes cannot be distinguished reliably
- a coarse scale would obscure safety-critical exceptions

## Scope

Canonical package: `drift-spectra-scaling@1.1.0`. ID: `T4-09`. Functional classes: drift-control, meta-control. Activation: `U2-specialized`. Mechanism basis: `normalized-from-recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- different task regions need different drift widths

## Non-Triggers

- every element has the same explicit tolerance
- classes cannot be distinguished reliably
- a coarse scale would obscure safety-critical exceptions

## Inputs / Required State

- content segments
- drift-band definitions
- consequence and authority assessment
- user transformation intent
- validation methods

## Outputs / Produced State

- content-to-band map
- validation allocation
- corridor initialization
- exception list

## Mechanism

Define a small ordered scale from zero movement through narrow paraphrase, bounded abstraction/reorganization, to explicitly creative variation. Classify content units by consequence, source authority, reversibility, and user intent; attach a validation method to every band, and promote exceptional high-risk units to a stricter band regardless of surrounding prose.

## Procedure

1. Define named drift bands and the semantic changes each permits.
2. Segment content into units whose tolerances can be assessed independently.
3. Score or judge consequence, authority, reversibility, and requested freedom.
4. Assign each unit to a band and specify its validation test.
5. Translate bands into controlled corridors and review effort.
6. Reclassify exceptions when evidence or task intent changes.

## Always-Do Rules

- define bands operationally
- classify at a useful content granularity
- attach a test to each band
- allow stricter local exceptions

## Never-Do / Avoid Rules

- treat the scale as aesthetic temperature
- average immutable and flexible content into one band
- use a higher band to permit unsupported facts

## Interaction Rules

### `controlled-drift-corridors`

Converts spectral bands into enforceable region boundaries.

### `zero-drift-zones`

Implements the strict endpoint for immutable units.

### `domain-normalized-drift`

Supplies a domain baseline before content-level classification.

## Compatible Upgradeables

- `controlled-drift-corridors` — Converts spectral bands into enforceable region boundaries.
- `zero-drift-zones` — Implements the strict endpoint for immutable units.
- `domain-normalized-drift` — Supplies a domain baseline before content-level classification.

## Counterbalancing Upgradeables

### `drift-suppression`

Catches actual outputs that do not match assigned bands.

### `clarification-gateway`

Clarifies intended flexibility when band assignment is consequential and ambiguous.

## Potential Redundancy

### `controlled-drift-corridors`

Spectra classify; corridors enforce. Store one classification-to-boundary mapping rather than duplicate policies.

### `compute-adaptive-drift`

Spectra concern content tolerance, not model strength or process overhead.

## Conflict / Precedence Rules

- Explicit source/task invariants override a permissive band assignment.
- When consequence classifications disagree, use the stricter band pending review.

## Failure Boundary

- Do not use a spectrum when bands lack observable distinctions.
- Escalate any unit whose risk cannot be classified and whose drift could cause harm.

## Strong-Model Scaling

May skip:

- numeric scoring when a direct band choice is obvious
- formal mapping for a uniform low-risk artifact

Keep mandatory:

- operational band definitions
- content-level exceptions
- no-new-claims boundary
- band-specific validation

## Recommended Skill Types

- mixed-content rewriting
- summaries
- format migrations
- multi-stage synthesis

## Example Composition

**Task context:** Convert a research paper into a public explainer.

**Why it activates:** Numbers and limitations must remain exact, explanations may simplify, and examples may be newly created if labeled.

**Inputs/state:** Paper sections, source authority, audience goal, and four defined drift bands.

**Action:** Maps measurements to zero, claims/limitations to narrow, organization to moderate, and labeled analogies to creative bands.

**Does not:** It does not give the entire explainer one creativity value.

**Result/state change:** Review effort and permitted transformation match each content type.

**Companions:** ['controlled-drift-corridors', 'zero-drift-zones', 'drift-suppression']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-09` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: DS-Scale.

Source support: `strongly-derivable`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — ECL / Drift Sink (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — Zero-drift (historical_assistant_artifact)
