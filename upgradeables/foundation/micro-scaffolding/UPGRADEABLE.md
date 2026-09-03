# Micro-Scaffolding

## Summary

A temporary, subtask-local checklist or mini-structure containing only the constraints and checkpoints most likely to be lost during the current step.

## Purpose

Protect a difficult local operation without loading the full OS, duplicating the parent StateBlock, or leaving permanent context residue.

## Problem Solved

Prevents a model from dropping a local requirement during a constrained rewrite, paragraph build, transformation, or multi-step judgment while avoiding heavyweight planning for simple work.

## Where It Fits in the OS

Roles: planning-reasoning, task-local state, execution support. Pipeline stages: pre-subtask planning, execution, subtask completion.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- high-constraint rewriting
- source-grounded paragraph construction
- localized code changes
- multi-step transformations
- complex formatting

## When Not to Use

- a one-step task has no fragile constraints
- the proposed scaffold repeats the full StateBlock or source corpus
- the subtask is already complete

## Scope

Canonical package: `micro-scaffolding@1.1.0`. ID: `T1-01`. Functional classes: planning-reasoning, state. Activation: `U0-foundational`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- Activate when the task requires multi-step or high-constraint work.

## Non-Triggers

- a one-step task has no fragile constraints
- the proposed scaffold repeats the full StateBlock or source corpus
- the subtask is already complete

## Inputs / Required State

- current subtask
- locked global constraints
- local failure risks
- relevant evidence pointers

## Outputs / Produced State

- temporary local checklist or mini-outline
- local verification result
- durable decisions promoted to StateBlock
- retirement marker

## Mechanism

At the start of a fragile subtask, extract only the few invariants and checkpoints that could be lost locally, such as preserve all numbers, preserve citation mapping, change tone only, and do not alter the conclusion. Use that compact scaffold while performing the step, check the local result against it, then retire the scaffold immediately when the subtask is accepted. It remains strictly smaller and shorter-lived than the workflow's canonical StateBlock.

## Procedure

1. Identify the current subtask and the specific failure risks within it.
2. Select the minimum local invariants, evidence pointers, and next-step checkpoints needed to control those risks.
3. Write a compact scaffold; do not copy unrelated global rules or full source material into it.
4. Execute the subtask while checking decisions against the scaffold.
5. Verify the local output against each scaffold item.
6. Merge only durable decisions into StateBlock, then delete or mark the temporary scaffold retired.

## Always-Do Rules

- Keep the scaffold task-local and smaller than canonical workflow state.
- Use concrete protected items rather than vague reminders.
- Retire it after the subtask so stale constraints cannot leak forward.

## Never-Do / Avoid Rules

- Do not expose private chain-of-thought.
- Do not build an elaborate visible plan for a trivial step.
- Do not let a local scaffold redefine global task authority or persist as canonical state.

## Interaction Rules

### `task-set-lock-in`

Supplies the global task contract from which the local scaffold selects only currently fragile invariants.

### `drift-suppression`

Uses the local checklist to detect divergence during execution and re-anchor without reloading the whole task.

### `working-memory-cues`

Can express the few scaffold items as concise active reminders while the subtask runs.

## Compatible Upgradeables

- `task-set-lock-in` — Supplies the global task contract from which the local scaffold selects only currently fragile invariants.
- `drift-suppression` — Uses the local checklist to detect divergence during execution and re-anchor without reloading the whole task.
- `working-memory-cues` — Can express the few scaffold items as concise active reminders while the subtask runs.

## Counterbalancing Upgradeables

### `cognitive-governor`

Suppresses unnecessary scaffold creation when the local risk does not justify the added structure.

## Potential Redundancy

### `stateblock`

StateBlock is durable canonical task state; Micro-Scaffolding is disposable subtask state and should not duplicate it.

### `working-memory-cues`

Cues are reminders; a micro-scaffold also defines a local sequence or acceptance checklist.

## Conflict / Precedence Rules

- Global task locks and source boundaries outrank a local scaffold.
- If the subtask expands into an architecture-level problem, retire the scaffold and re-plan at the parent task level.

## Failure Boundary

- Escalate when the required control cannot remain local or when the scaffold grows into a duplicate of the parent plan/state.
- Reject the local result if any protected item was lost or changed without authorization.

## Strong-Model Scaling

May skip:

- writing the scaffold out when two or three local invariants can be held reliably
- multiple framing candidates for a routine paragraph

Keep mandatory:

- identify the fragile local invariants
- verify them after the step
- retire temporary scaffolding

## Recommended Skill Types

- analysis and decision support
- communication and content generation
- document and code transformation
- long-context workflows

## Example Composition

**Task context:** Rewrite one evidence-heavy paragraph for clarity.

**Why it activates:** Numbers, citations, and conclusion must remain unchanged while prose changes.

**Inputs/state:** Original paragraph plus four protected items: preserve numbers, citation-to-claim mapping, conclusion, and factual modality.

**Action:** Creates the four-item local checklist, rewrites, verifies each item, promotes no new global state, and retires the checklist.

**Does not:** It does not reload the full paper, invent a new outline, or keep the checklist active for later sections.

**Result/state change:** A clearer paragraph with all four invariants intact and no stale scaffold.

**Companions:** ['task-set-lock-in', 'drift-suppression', 'safe-rewrite']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T1-01` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: Micro-Scaffolding (Planning Before Writing).

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.5 Section / paragraph micro-scaffolding (historical_assistant_artifact)
- OS_Upgradeables_Historical_Recovery_Inventory.md — January 5 scaffolding classification (historical_recovery_inventory)
