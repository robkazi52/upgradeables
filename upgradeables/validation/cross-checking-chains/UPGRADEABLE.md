# Cross-Checking Chains

## Summary

Verifies a claim through an explicit sequence of differently purposed checks, where each link consumes the prior link's evidence and failure state.

## Purpose

Make validation ordered, traceable, and resistant to repeated correlated checking.

## Problem Solved

A pile of nominal checks can repeat the same assumption, omit prerequisites, or allow later confidence to obscure an earlier failure.

## Where It Fits in the OS

Roles: ordered-validation-orchestrator, evidence-handoff-chain. Pipeline stages: verification planning, sequential validation, final collapse.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- high-stakes fact verification
- data pipeline validation
- release qualification
- multi-source research

## When Not to Use

- one direct authoritative check fully resolves a low-risk atom
- checks cannot be ordered by dependency

## Scope

Canonical package: `cross-checking-chains@1.1.0`. ID: `T3-07`. Functional classes: validation. Activation: `U2-specialized`. Mechanism basis: `recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- a conclusion relies on a dependency chain

## Non-Triggers

- one direct authoritative check fully resolves a low-risk atom
- checks cannot be ordered by dependency

## Inputs / Required State

- critical claim
- ordered check specification
- evidence sources
- resolution rules

## Outputs / Produced State

- link-by-link ledger
- typed failure location
- resolved or blocked verdict

## Mechanism

Design a chain whose links have distinct jobs—such as identity/provenance, extraction, entailment, independent corroboration, and consequence testing. Each link receives the claim plus the prior evidence ledger, may add evidence or a typed failure, and cannot erase an upstream failure; certification requires every mandatory link to pass or an explicit resolution branch to close the discrepancy.

## Procedure

1. Select the critical claim or atom.
2. Enumerate its verification dependencies in causal order.
3. Assign each link a distinct evidence source or validation lens.
4. Define required input, pass condition, and typed failure for every link.
5. Run links in order and preserve the accumulating ledger.
6. Route discrepancies to repair or independent adjudication.
7. Collapse only after all mandatory links and resolutions are complete.

## Always-Do Rules

- Test independence between links that claim corroboration.
- Carry upstream failures forward visibly.
- Define an endpoint and mandatory links before running.

## Never-Do / Avoid Rules

- Count repeated use of one source as multiple corroborations.
- Let a downstream style or plausibility check erase a provenance failure.
- Extend the chain without a decision-relevant reason.

## Interaction Rules

### `critical-atomic-verification`

Selects the decisive atoms around which chains are built.

### `truth-redundancy`

Supplies independent corroboration for a chain link.

### `citation-fidelity`

Can serve as the evidence-entailment link.

## Compatible Upgradeables

- `critical-atomic-verification` — Selects the decisive atoms around which chains are built.
- `truth-redundancy` — Supplies independent corroboration for a chain link.
- `citation-fidelity` — Can serve as the evidence-entailment link.

## Counterbalancing Upgradeables

### `bounded-exit`

Limits chain expansion and terminates unresolved cycles.

## Potential Redundancy

### `parallel-qms`

A chain is dependency-ordered and state-carrying; Parallel QMS runs selectable independent or orthogonal validator modes.

## Conflict / Precedence Rules

- Prerequisite failure blocks dependent links from certifying the claim.
- A disagreement between independent links requires explicit resolution, not majority counting.

## Failure Boundary

- Do not certify when a mandatory link fails, is skipped, or depends on the same untested assumption as its supposed corroborator.

## Strong-Model Scaling

May skip:

- non-material optional links once the declared endpoint is met

Keep mandatory:

- dependency order
- link independence
- failure propagation

## Recommended Skill Types

- high-stakes fact verification
- data pipeline validation
- release qualification
- multi-source research

## Example Composition

**Task context:** A dataset row is used to justify a product safety claim.

**Why it activates:** Identity, extraction, interpretation, and corroboration must all hold in order.

**Inputs/state:** Dataset version, row locator, calculation, paper, and safety threshold.

**Action:** Checks artifact identity, recomputes the value, tests claim entailment, then corroborates with an independent source.

**Does not:** Count two pages quoting the same dataset as independent proof.

**Result/state change:** The chain stops at a unit mismatch before the unsafe conclusion is released.

**Companions:** ['critical-atomic-verification', 'citation-fidelity', 'truth-redundancy']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-07` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T3-07. Cross-Checking Chains (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — T3-07. Cross-Checking Chains (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 8.1 QMS-M (historical_assistant_artifact)
