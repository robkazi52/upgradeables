# Task-Set Lock-In

## Summary

Freeze the clarified objective, deliverables, acceptance criteria, constraints, and out-of-scope items as the active task contract.

## Purpose

Prevent scope substitution and goal drift during execution.

## Problem Solved

A model can optimize a nearby but different problem, quietly add deliverables, or forget the success criteria after extensive context.

## Where It Fits in the OS

Roles: task identity, scope control, acceptance gate. Pipeline stages: after clarification, before planning, at scope-change requests, final acceptance.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-step builds
- contracted deliverables
- long research
- tasks with exclusions

## When Not to Use

- the task is still materially ambiguous
- open-ended ideation intentionally has no fixed deliverable
- the user explicitly authorizes dynamic exploration

## Scope

Canonical package: `task-set-lock-in@1.1.0`. ID: `T1-06`. Functional classes: framing-intake, state. Activation: `U0-foundational`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- multi-step work begins or scope changes

## Non-Triggers

- the task is still materially ambiguous
- open-ended ideation intentionally has no fixed deliverable
- the user explicitly authorizes dynamic exploration

## Inputs / Required State

- clarified request
- deliverables
- constraints
- acceptance criteria
- non-goals
- change authority

## Outputs / Produced State

- versioned task-set contract
- scope-gated plan
- acceptance checklist
- scope-change record

## Mechanism

Convert the clarified request into a compact task-set contract: primary objective, required outputs, quality gates, constraints, non-goals, dependencies, and change authority. Check each planned action and final artifact against it; update only through an explicit, versioned scope-change decision.

## Procedure

1. Extract the objective, required artifacts, constraints, success tests, and exclusions.
2. Resolve material ambiguity before locking.
3. Record the task set as locked fields with a version and change authority.
4. Gate planned actions and newly proposed work against the set.
5. For legitimate changes, record the requester, rationale, and new version.
6. Use acceptance criteria to close the task.

## Always-Do Rules

- include non-goals
- define completion evidence
- record authorized scope changes
- check final output against the locked set

## Never-Do / Avoid Rules

- lock unresolved ambiguity
- expand scope because related work is interesting
- silently weaken acceptance criteria

## Interaction Rules

### `clarification-gateway`

Produces the unambiguous task set that can safely be locked.

### `mode-lock-in`

Stabilizes the operating method used for the locked task.

### `stateblock`

Stores the task set as protected canonical fields.

## Compatible Upgradeables

- `clarification-gateway` — Produces the unambiguous task set that can safely be locked.
- `mode-lock-in` — Stabilizes the operating method used for the locked task.
- `stateblock` — Stores the task set as protected canonical fields.

## Counterbalancing Upgradeables

### `micro-scaffolding`

Allows disposable local structure inside the fixed task without expanding the task itself.

### `controlled-drift-corridors`

Permits explicitly bounded flexibility in parts of the deliverable.

## Potential Redundancy

### `mode-lock-in`

Combine overlapping contract fields but preserve the what-versus-how distinction.

### `working-memory-lock-in`

Refresh a pointer or small critical subset rather than copying the entire task set.

## Conflict / Precedence Rules

- System and latest explicit authorized user scope changes override older task-set versions.
- When a new request conflicts with locked acceptance criteria, pause for a scope-change decision.

## Failure Boundary

- Do not claim completion when a required artifact or quality gate lacks evidence.
- Unlock and clarify when task identity changes materially.

## Strong-Model Scaling

May skip:

- formal serialization for a tiny clear request
- repeating the full contract during every action

Keep mandatory:

- objective
- required deliverables
- constraints and non-goals
- acceptance evidence
- explicit change control

## Recommended Skill Types

- long-context workflows
- multi-step task execution
- skill and agent workflows
- source-grounded research

## Example Composition

**Task context:** Build and validate a public repository without changing the canonical source files.

**Why it activates:** Many attractive documentation additions could distract from required build and validation outputs.

**Inputs/state:** Required repository, validation gates, immutable source constraint, and publication condition.

**Action:** Locks those fields, gates work against them, and records any user-authorized scope change.

**Does not:** It does not stop after scaffolding or rewrite the source corpus.

**Result/state change:** Completion is evaluated against the original concrete specification.

**Companions:** ['clarification-gateway', 'mode-lock-in', 'stateblock']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T1-06` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 3. November 28, 2025 — frozen Tier-2 master set (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 8. Working-Memory Lock-In Heartbeats (historical_assistant_artifact)
