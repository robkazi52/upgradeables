# Contradiction Micro-Repair Pack

## Summary

Repairs the smallest region responsible for a contradiction and rechecks both statements without rewriting unrelated content.

## Purpose

Resolve direct logical or factual inconsistency while preserving every compatible claim and locked constraint.

## Problem Solved

A document or state can contain two claims that cannot both hold, yet broad rewriting risks erasing the supported one or creating new drift.

## Where It Fits in the OS

Roles: contradiction-specific repair pack, local consistency restorer. Pipeline stages: consistency validation, localized repair, post-repair verification.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- conflicting requirements
- inconsistent dates or quantities
- state snapshots with mutually exclusive flags
- documents whose conclusion contradicts a cited premise

## When Not to Use

- the apparent contradiction is a legitimate difference in scope or time
- the conflict spans the artifact's governing architecture
- neither side can be adjudicated from available authority

## Scope

Canonical package: `contradiction-micro-repair@1.1.0`. ID: `T4-04`. Functional classes: editing-repair, validation. Activation: `U1-common-conditional`. Mechanism basis: `normalized-from-recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- a localized contradiction is detected

## Non-Triggers

- the apparent contradiction is a legitimate difference in scope or time
- the conflict spans the artifact's governing architecture
- neither side can be adjudicated from available authority

## Inputs / Required State

- candidate conflicting claims
- provenance
- scope and time qualifiers
- locked constraints

## Outputs / Produced State

- contradiction determination
- minimal adjudicated patch or explicit unresolved conflict
- two-sided verification

## Mechanism

Represent the conflict as claim A, claim B, and the condition under which they cannot coexist; inspect scope, time, modality, and authority to decide whether it is real. If real and locally adjudicable, patch only the unsupported or misstated unit, then retest the pair and nearby dependents. If authority is insufficient, preserve the conflict explicitly instead of choosing by fluency.

## Procedure

1. Extract the two conflicting claims and their provenance.
2. Normalize their scope, time, subject, quantity, and modality to confirm a true contradiction.
3. Determine which claim is locked, better supported, or requires escalation.
4. Edit the smallest clause, field, or local rule that resolves the inconsistency.
5. Re-evaluate both claims and any directly dependent conclusion; report unresolved conflict when evidence cannot adjudicate.

## Always-Do Rules

- prove the contradiction before editing
- preserve the better-supported or locked claim
- recheck both sides and direct dependents

## Never-Do / Avoid Rules

- flatten legitimate perspectives into one claim
- silently choose a side without authority
- rewrite unrelated sections to make the artifact sound consistent

## Interaction Rules

### `micro-repair`

Micro-Repair supplies the minimal patch discipline after the contradiction is localized.

### `bidirectional-consistency`

Bidirectional Consistency can detect whether upstream and downstream claims disagree in both directions.

## Compatible Upgradeables

- `micro-repair` — Micro-Repair supplies the minimal patch discipline after the contradiction is localized.
- `bidirectional-consistency` — Bidirectional Consistency can detect whether upstream and downstream claims disagree in both directions.

## Counterbalancing Upgradeables

### `multi-truth-gating`

Multi-Truth Gating prevents repair when claims are merely different scoped truths rather than contradictions.

## Potential Redundancy

### `micro-repair`

Micro-Repair handles any local defect; this pack adds contradiction normalization, authority adjudication, and two-sided retesting.

## Conflict / Precedence Rules

- A source-locked claim outranks an unsupported generated claim.
- If two authoritative sources genuinely conflict, do not edit one away; expose and route the conflict.
- Scope- or time-qualified differences are preserved, not repaired.

## Failure Boundary

- false contradiction from different scopes
- unsupported winner selection
- collateral rewrite
- repair that leaves a dependent contradiction

## Strong-Model Scaling

May skip:

- formal claim notation when the conflict is an obvious local typo

Keep mandatory:

- scope normalization
- authority check
- two-sided post-repair test

## Recommended Skill Types

- document and code transformation
- high-stakes evidence work
- review and quality assurance

## Example Composition

**Task context:** A report says a pilot starts in June and later says it concluded in May of the same year.

**Why it activates:** The dates are mutually incompatible under the same pilot identity and year.

**Inputs/state:** The approved schedule says the pilot starts in March and ends in May; the June sentence is generated prose.

**Action:** Confirms same scope and year, replaces June with March in the single clause, and rechecks the timeline and conclusion.

**Does not:** Rewrite the entire schedule section or preserve both dates as perspectives.

**Result/state change:** One local correction with timeline consistency restored.

**Companions:** ['micro-repair', 'bidirectional-consistency']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-04` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `strongly-derivable`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 10. Tier-4 / Meta-Supervisor recovered family (historical_recovery_inventory)
