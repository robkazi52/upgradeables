# HYBRID Mode

## Summary

Uses POWER for bounded design exploration, then crosses an explicit supervisor gate into SAFE for grounded execution.

## Purpose

Combine broad planning capability with conservative implementation without letting speculative branch assumptions leak into committed work.

## Problem Solved

A workflow often needs creative architecture search and precise execution, but one undifferentiated mode either narrows planning too early or executes unverified ideas too freely.

## Where It Fits in the OS

Roles: dual-mode workflow, planning-to-execution transition controller. Pipeline stages: POWER planning, collapse and handoff, SAFE execution, post-execution validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- architecture followed by implementation
- research plan followed by evidence extraction
- migration design followed by cutover
- complex repository builds

## When Not to Use

- the task needs only narrow execution
- the task is pure open exploration with no commitment
- no supervisor can define and validate the transition state

## Scope

Canonical package: `hybrid-mode@1.1.0`. ID: `T4-08`. Functional classes: meta-control, orchestration. Activation: `U4-meta-architecture`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- work includes both broad design and grounded execution

## Non-Triggers

- the task needs only narrow execution
- the task is pure open exploration with no commitment
- no supervisor can define and validate the transition state

## Inputs / Required State

- task and constraints
- planning rubric
- transition-state schema
- execution evidence
- supervisor authority

## Outputs / Produced State

- selected plan
- validated POWER-to-SAFE handoff
- grounded execution result
- mode-transition record

## Mechanism

Run POWER only to generate and compare bounded plans, then collapse to one plan and construct a handoff containing locked goals, selected decisions, rejected assumptions, evidence needs, risks, and execution invariants. A supervisor validates the handoff before activating SAFE, which executes only the committed plan with narrow drift and atomic checks. Re-enter POWER only through a checkpoint when execution exposes an architecture-level defect.

## Procedure

1. Declare HYBRID and define separate planning and execution completion criteria.
2. Use POWER to generate, evaluate, and collapse candidate plans.
3. Create a transition state with the selected plan, locked constraints, evidence, risks, unresolved items, and retired branches.
4. Have the supervisor verify that the plan is executable and no speculative assumptions remain active.
5. Switch explicitly to SAFE and execute with grounding, narrow drift, and atomic validation.
6. If execution uncovers a design failure, checkpoint state and deliberately return to POWER rather than improvising.

## Always-Do Rules

- declare the active phase
- collapse branches before execution
- transfer locked state explicitly
- gate every POWER-to-SAFE and SAFE-to-POWER transition

## Never-Do / Avoid Rules

- execute directly from multiple POWER branches
- carry exploratory assumptions into SAFE as facts
- silently switch modes mid-action
- use HYBRID when one mode suffices

## Interaction Rules

### `power-mode`

POWER supplies bounded design and candidate comparison in the first phase.

### `safe-mode`

SAFE supplies grounded, conservative execution after commitment.

### `ultimate-suite-supervisor`

The suite supervisor owns phase declaration, conflict resolution, and transition authorization.

## Compatible Upgradeables

- `power-mode` — POWER supplies bounded design and candidate comparison in the first phase.
- `safe-mode` — SAFE supplies grounded, conservative execution after commitment.
- `ultimate-suite-supervisor` — The suite supervisor owns phase declaration, conflict resolution, and transition authorization.

## Counterbalancing Upgradeables

### `meta-stability`

Meta-Stability can freeze transition state when repeated mode switching threatens coherence.

## Potential Redundancy

### `power-mode`

POWER alone does not define the safe execution transition.

### `safe-mode`

SAFE alone does not provide broad architectural search.

## Conflict / Precedence Rules

- No POWER branch may execute until one plan passes collapse and handoff validation.
- SAFE findings can reopen design only through a recorded checkpoint.
- Truth and safety vetoes survive both modes and cannot be relaxed by transition.

## Failure Boundary

- mode leakage
- uncollapsed execution
- lost constraints at handoff
- silent oscillation
- POWER used to bypass SAFE evidence rules

## Strong-Model Scaling

May skip:

- verbose phase narration for a compact two-step task

Keep mandatory:

- explicit collapse
- handoff state
- supervisor gate
- narrow execution

## Recommended Skill Types

- high-stakes evidence work
- multi-step task execution
- skill and agent workflows
- source-grounded research

## Example Composition

**Task context:** Design and publish a new plugin architecture.

**Why it activates:** Several architectures deserve exploration, but repository edits and publication require precise validated execution.

**Inputs/state:** Requirements, candidate patterns, validation suite, and publishing authority are known.

**Action:** Uses POWER for three architectures, collapses to one, records interfaces and rejected assumptions, then switches to SAFE for file edits, tests, and publication.

**Does not:** Mix components from losing designs during implementation without reopening the design gate.

**Result/state change:** Broad design quality with a controlled, auditable execution path.

**Companions:** ['power-mode', 'safe-mode', 'ultimate-suite-supervisor']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-08` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 10. Tier-4 / Meta-Supervisor recovered family (historical_recovery_inventory)
