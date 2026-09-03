# Micro-Repair

## Summary

Corrects the smallest faulty unit while freezing all correct surrounding content.

## Purpose

Restore local correctness or completeness with the minimum semantic blast radius.

## Problem Solved

Models often answer a one-clause, one-transition, or one-format defect with a wholesale rewrite that damages accepted material.

## Where It Fits in the OS

Roles: local repair primitive, minimal-change editor. Pipeline stages: defect localization, local correction, neighborhood recheck.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- one unsupported claim
- one missing requirement
- awkward transition
- local contradiction
- small formatting defect

## When Not to Use

- the artifact architecture is globally wrong
- the same defect repeats systemically
- the correct local replacement depends on unresolved global decisions

## Scope

Canonical package: `micro-repair@1.1.0`. ID: `T2-04`. Functional classes: editing-repair. Activation: `U0-foundational`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- Activate when the task requires a defect is localized.

## Non-Triggers

- the artifact architecture is globally wrong
- the same defect repeats systemically
- the correct local replacement depends on unresolved global decisions

## Inputs / Required State

- artifact
- localized failed criterion
- frozen surrounding atoms
- replacement evidence

## Outputs / Produced State

- minimal patch
- changed-atom list
- local boundary validation
- escalation signal if systemic

## Mechanism

Define a repair window around the smallest unit that fails an explicit criterion, freeze the surrounding accepted region, patch only that unit and any directly required connective token, then compare the window before and after. Widen once only when a direct dependency proves the first window insufficient; recurring or architecture-level failure escalates instead of allowing scope creep.

## Procedure

1. Identify the exact failed criterion and the smallest text, field, rule, or code unit causing it.
2. Mark the surrounding accepted content and locked facts as frozen.
3. Draft the smallest replacement that satisfies the criterion.
4. Check boundary coherence with the immediately preceding and following units.
5. Verify the target defect is gone and no frozen atom changed.
6. If repair requires broad movement or repeats elsewhere, stop and route to Structured Refinement, Regenerative Rewrite, or Surgery.

## Always-Do Rules

- name the defect before patching
- freeze correct surroundings
- compare changed atoms
- recheck both local boundaries

## Never-Do / Avoid Rules

- rewrite for style outside the repair window
- expand scope because adjacent prose could also be improved
- use local repair to conceal systemic failure

## Interaction Rules

### `safe-rewrite`

Safe Rewrite preserves factual atoms when the micro-repair changes wording.

### `invariance-stress-scaffold`

Invariance Stress verifies frozen neighbors and facts remain unchanged.

### `contradiction-micro-repair`

The contradiction pack adds conflict adjudication when the localized defect is inconsistency.

## Compatible Upgradeables

- `safe-rewrite` — Safe Rewrite preserves factual atoms when the micro-repair changes wording.
- `invariance-stress-scaffold` — Invariance Stress verifies frozen neighbors and facts remain unchanged.
- `contradiction-micro-repair` — The contradiction pack adds conflict adjudication when the localized defect is inconsistency.

## Counterbalancing Upgradeables

### `regenerative-rewrite`

Regenerative Rewrite is the correct escalation when local patches cannot restore global structure.

### `surgery-edit`

Surgery replaces architecture when the defect is structural rather than local.

## Potential Redundancy

### `crispr-edit`

Both are precise; Micro-Repair is the general smallest-fault correction, while CRISPR uses a formal patch contract for structured systems.

### `safe-rewrite`

Safe Rewrite governs dimensions of prose transformation; Micro-Repair governs defect scope.

## Conflict / Precedence Rules

- Do not preserve a frozen neighbor if it is proven part of the defect; explicitly widen the window instead.
- A locked invariant outranks local fluency.
- After one justified scope expansion, recurring failure triggers escalation rather than further widening.

## Failure Boundary

- scope creep
- cosmetic rewriting around a defect
- repair that breaks a neighboring transition
- serial local patches to a global architecture failure

## Strong-Model Scaling

May skip:

- explicitly printing the frozen-region list for an obvious typo

Keep mandatory:

- smallest-fault localization
- changed-atom comparison
- systemic-failure escalation

## Recommended Skill Types

- one unsupported claim
- one missing requirement
- awkward transition
- local contradiction
- small formatting defect

## Example Composition

**Task context:** A grant narrative contains one unsupported sentence between two accepted paragraphs.

**Why it activates:** The defect is local and the surrounding argument is correct.

**Inputs/state:** The sentence overstates the cited study; the source supports a narrower claim.

**Action:** Freezes both paragraphs, replaces only the overstated clause with source-supported wording, and checks both transitions and citation fit.

**Does not:** Reframe the whole section or add new evidence claims.

**Result/state change:** The unsupported claim is removed with no unrelated semantic change.

**Companions:** ['safe-rewrite', 'citation-fidelity']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-04` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T2-04. Micro-Repair (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 1. Canonical current consolidated inventory (historical_recovery_inventory)
