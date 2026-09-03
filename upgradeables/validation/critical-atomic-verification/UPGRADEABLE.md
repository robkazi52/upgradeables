# Critical Atomic Verification

## Summary

Decomposes a high-stakes conclusion into indispensable truth atoms and verifies each atom before allowing the conclusion to stand.

## Purpose

Concentrate verification on the smallest facts whose failure would invalidate the output.

## Problem Solved

Whole-answer review can pass because most content is correct even though one decisive date, number, identity, precondition, or negation is wrong.

## Where It Fits in the OS

Roles: critical-atom-verifier, claim-decomposition-gate. Pipeline stages: pre-commitment, evidence validation, pre-release.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- medical or legal factual synthesis
- deployment decisions
- financial calculations
- requirements verification
- citation-heavy research

## When Not to Use

- no factual conclusion or consequential action depends on the output
- the content is purely expressive

## Scope

Canonical package: `critical-atomic-verification@1.1.0`. ID: `T3-04`. Functional classes: validation, truth-grounding. Activation: `U3-high-risk-expensive`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- small factual errors could change the outcome

## Non-Triggers

- no factual conclusion or consequential action depends on the output
- the content is purely expressive

## Inputs / Required State

- candidate conclusion
- claim dependency graph
- risk tier
- evidence sources

## Outputs / Produced State

- critical-atom ledger
- evidence status per atom
- recomputed conclusion
- repair or abstention decision

## Mechanism

Build a dependency graph from the intended conclusion back to minimal truth-bearing atoms. Mark an atom critical when its falsity, reversal, or absence would change the conclusion or safe action. Verify every critical atom directly at depth proportional to risk; propagate any failed or unknown atom forward so the dependent conclusion is repaired, qualified, or blocked.

## Procedure

1. State the conclusion or action being certified.
2. Decompose it into atomic claims and dependencies.
3. Use a removal or reversal test to mark critical atoms.
4. Assign verification depth and evidence requirements by consequence.
5. Verify each critical atom independently and record true, false, unknown, or conflicting.
6. Recompute the conclusion from verified states.
7. Block, repair, or qualify conclusions that depend on false or unresolved critical atoms.

## Always-Do Rules

- Include qualifiers, negations, units, dates, and identities as atoms when material.
- Propagate uncertainty from atom to conclusion.
- Verify critical atoms with direct evidence where available.

## Never-Do / Avoid Rules

- Average a failed critical atom into an overall high score.
- Treat fluent wording as evidence.
- Hide an unresolved atom inside a broad paragraph-level pass.

## Interaction Rules

### `citation-fidelity`

Audits whether cited evidence truly supports each atom.

### `risk-tier-scaling`

Sets verification depth for each atom.

### `cross-checking-chains`

Adds ordered independent checks to especially consequential atoms.

## Compatible Upgradeables

- `citation-fidelity` — Audits whether cited evidence truly supports each atom.
- `risk-tier-scaling` — Sets verification depth for each atom.
- `cross-checking-chains` — Adds ordered independent checks to especially consequential atoms.

## Counterbalancing Upgradeables

### `dynamic-depth-allocation`

Prevents equal-cost verification of noncritical atoms.

## Potential Redundancy

### `multi-truth-gating`

Multi-Truth arbitrates candidate truths; CAV identifies and verifies the indispensable atoms within a conclusion.

## Conflict / Precedence Rules

- A false critical atom vetoes any dependent conclusion.
- An unknown critical atom requires qualification or abstention, not a guessed value.
- Direct source evidence outranks derived narrative confidence.

## Failure Boundary

- Do not certify a conclusion while any indispensable atom is false, materially conflicting, or unsupported beyond the allowed risk threshold.

## Strong-Model Scaling

May skip:

- formal graph notation for a low-complexity claim

Keep mandatory:

- criticality test
- atom-wise evidence status
- uncertainty propagation

## Recommended Skill Types

- analysis and decision support
- high-stakes evidence work
- review and quality assurance
- source-grounded research

## Example Composition

**Task context:** A release note claims a migration is backward compatible.

**Why it activates:** One removed field or changed default would invalidate the consequential conclusion.

**Inputs/state:** Compatibility claim, schema diff, supported-version contract, and tests.

**Action:** Atomizes field presence, defaults, serialization, and version handling; finds the changed default critical.

**Does not:** Approve because most integration tests pass.

**Result/state change:** The compatibility claim is blocked until the default is restored or documented as breaking.

**Companions:** ['citation-fidelity', 'risk-tier-scaling', 'cross-checking-chains']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-04` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 1. Canonical current consolidated inventory (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.1 Source atomization (historical_assistant_artifact)
