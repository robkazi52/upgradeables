# StateBlock

## Summary

Maintain one canonical, schema-defined representation of the task's current operational state.

## Purpose

Give tools, agents, validators, and handoffs a shared source of current task truth.

## Problem Solved

Critical constraints, progress, decisions, and open issues otherwise remain scattered across prose and become inconsistent.

## Where It Fits in the OS

Roles: canonical state model, coordination substrate, validation target. Pipeline stages: task initialization, after accepted state changes, before action, handoff and recovery.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-step execution
- agent orchestration
- complex editing
- auditable workflows

## When Not to Use

- a trivial one-turn task needs no persistent state
- the proposed schema would collect unnecessary sensitive data
- multiple writers cannot coordinate versions

## Scope

Canonical package: `stateblock@1.1.0`. ID: `T2-09`. Functional classes: state. Activation: `U0-foundational`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- work spans multiple steps or components

## Non-Triggers

- a trivial one-turn task needs no persistent state
- the proposed schema would collect unnecessary sensitive data
- multiple writers cannot coordinate versions

## Inputs / Required State

- clarified task contract
- authority hierarchy
- state schema
- evidence references
- accepted deltas

## Outputs / Produced State

- versioned canonical state
- field-level provenance
- consumer projections
- validation surface

## Mechanism

Define a typed block with identity, objective, authority, constraints, active mode, progress, evidence pointers, decisions, uncertainties, open actions, and version metadata. Assign each field an owner and mutability rule; update through validated deltas, and derive views from this block so no consumer silently becomes a second authority.

## Procedure

1. Select only fields required to execute and verify the task.
2. Declare field types, authority, mutability, and sensitivity.
3. Initialize values from clarified instructions and canonical sources.
4. Route changes through validated versioned deltas.
5. Expose least-privilege projections to consumers.
6. Validate outputs against current locked fields and checkpoint major versions.

## Always-Do Rules

- maintain one canonical owner
- version meaningful changes
- label unknown and unresolved fields
- protect authority-bearing values

## Never-Do / Avoid Rules

- duplicate divergent canonical blocks
- silently fill unknown fields
- let untrusted content rewrite task authority
- store unnecessary secrets

## Interaction Rules

### `sequential-memory-state-engine`

Provides the ordered mutation lifecycle.

### `selfblock-auto-update`

Applies safe bounded deltas after events.

### `structured-state-projection`

Creates consumer-specific views without duplicating ownership.

## Compatible Upgradeables

- `sequential-memory-state-engine` — Provides the ordered mutation lifecycle.
- `selfblock-auto-update` — Applies safe bounded deltas after events.
- `structured-state-projection` — Creates consumer-specific views without duplicating ownership.

## Counterbalancing Upgradeables

### `micro-scaffolding`

Uses a lighter disposable structure before information deserves promotion to canonical state.

### `working-memory-cues`

Keeps attention on a few fields without repeatedly loading the whole block.

## Potential Redundancy

### `cot-structured-state-block`

Embed the structured reasoning view or derive it; do not create a competing source of task truth.

### `task-set-lock-in`

Represent the locked task subset inside StateBlock rather than separately.

## Conflict / Precedence Rules

- System and explicit task authority govern locked fields; evidence updates factual fields only through their declared owners.
- Version conflicts must be resolved before action; never merge incompatible values by concatenation.

## Failure Boundary

- Do not proceed on dependent actions when required state is contradictory or unknown.
- Fall back to an explicit local checklist if the host cannot maintain a reliable shared block.

## Strong-Model Scaling

May skip:

- a formal serialized object for a tiny task
- unused optional fields

Keep mandatory:

- single source of truth
- locked-field authority
- explicit unknowns
- versioned updates

## Recommended Skill Types

- multi-step execution
- agent orchestration
- complex editing
- auditable workflows

## Example Composition

**Task context:** Three agents prepare, review, and publish a technical report.

**Why it activates:** They need a shared current objective, source set, status, and unresolved-risk record.

**Inputs/state:** Approved scope, authority rules, section owners, evidence index, and publish gate.

**Action:** Creates one versioned block and gives each agent a scoped view with controlled update rights.

**Does not:** It does not let each agent maintain an independent final status.

**Result/state change:** Coordination and validation use the same current task truth.

**Companions:** ['sequential-memory-state-engine', 'structured-state-projection', 'state-snapshot']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-09` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — StateBlock (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — Interpretation rule for the frozen T2 registry (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — T2-038 — High-Coherence State Induction (historical_assistant_artifact)
