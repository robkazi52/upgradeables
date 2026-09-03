# Coherence Loops

## Summary

A bounded diagnose-repair-recheck cycle for restoring global agreement after a coherence discrepancy is detected.

## Purpose

Repair cross-part inconsistencies while preventing endless self-review.

## Problem Solved

A single patch can move contradictions elsewhere, while unbounded reflection consumes effort without a convergence rule.

## Where It Fits in the OS

Roles: global-consistency-repair-loop, bounded-convergence-controller. Pipeline stages: integration, post-drift-detection, pre-release.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-file changes
- long-form documents
- multi-agent synthesis
- cross-component specification repair

## When Not to Use

- the discrepancy is isolated and a single deterministic correction suffices
- no stable acceptance criteria exist

## Scope

Canonical package: `coherence-loops@1.1.0`. ID: `A-11`. Functional classes: validation, editing-repair. Activation: `U2-specialized`. Mechanism basis: `recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- local edits risk global inconsistency

## Non-Triggers

- the discrepancy is isolated and a single deterministic correction suffices
- no stable acceptance criteria exist

## Inputs / Required State

- coherence discrepancy
- governing invariants
- dependency map
- iteration budget
- acceptance checks

## Outputs / Produced State

- repaired coherent state
- iteration ledger
- non-convergence report
- external decision request

## Mechanism

Freeze the governing invariants, locate the smallest inconsistent dependency set, repair the highest-leverage cause, and rerun checks across affected boundaries. Continue only while measured inconsistency decreases; stop on verified convergence, a fixed iteration/depth budget, repeated unchanged failure, or a conflict requiring external authority.

## Procedure

1. Record the detected inconsistency and governing invariants.
2. Trace affected dependencies and identify the earliest causal mismatch.
3. Choose the smallest repair expected to restore the widest agreement.
4. Apply or propose the repair and rerun local plus boundary checks.
5. Compare residual inconsistency with the prior iteration.
6. Exit on convergence; otherwise iterate within the explicit budget.
7. On non-convergence, return the stable conflict and required decision instead of looping.

## Always-Do Rules

- Set exit criteria before iterating.
- Recheck dependent boundaries after each repair.
- Preserve an audit trail of changed assumptions.

## Never-Do / Avoid Rules

- Repeat reflection with no changed hypothesis or evidence.
- Declare convergence because the iteration budget expired.
- Repair symptoms while ignoring a known upstream cause.

## Interaction Rules

### `coherence-heartbeat`

Supplies discrepancy signals that justify a deeper loop.

### `bounded-exit`

Enforces convergence and stop conditions.

### `reflectos`

Adds reflective comparison of intended and actual process when the inconsistency is procedural.

## Compatible Upgradeables

- `coherence-heartbeat` — Supplies discrepancy signals that justify a deeper loop.
- `bounded-exit` — Enforces convergence and stop conditions.
- `reflectos` — Adds reflective comparison of intended and actual process when the inconsistency is procedural.

## Counterbalancing Upgradeables

### `crispr-edit`

Prevents a coherence repair from expanding beyond the smallest causal edit.

## Potential Redundancy

### `coherence-heartbeat`

The heartbeat monitors; the loop performs bounded causal repair.

## Conflict / Precedence Rules

- Explicit invariants outrank local convenience.
- If repairs oscillate between two states, stop and expose the underlying unresolved tradeoff.

## Failure Boundary

- Stop without certification when inconsistency does not decrease, repairs oscillate, or resolution requires changing a locked invariant.

## Strong-Model Scaling

May skip:

- multiple iterations after the first repair fully satisfies all boundary checks

Keep mandatory:

- explicit invariants, dependency recheck, and bounded exit

## Recommended Skill Types

- document and code transformation
- high-stakes evidence work
- long-context workflows
- review and quality assurance

## Example Composition

**Task context:** A schema rename fixes code but leaves documentation, fixtures, and a contribution template inconsistent.

**Why it activates:** The defect spans dependent artifacts and one repair may expose another.

**Inputs/state:** Rename invariant, affected-file map, validation commands, and a three-pass budget.

**Action:** Repairs the schema source, regenerates dependents, checks docs and fixtures, then exits when all agree.

**Does not:** Keep rewriting unrelated prose after convergence.

**Result/state change:** All surfaces use one schema name with a recorded two-iteration repair path.

**Companions:** ['coherence-heartbeat', 'bounded-exit', 'crispr-edit']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `A-11` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 11. Advanced architecture Upgradeables retained (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 11.6 Refinement (historical_assistant_artifact)
