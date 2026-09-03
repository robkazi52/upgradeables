# SAFE Mode

## Summary

Executes a committed task with narrow drift, strong grounding, atomic verification, conservative output, and fail-closed handling of unavailable evidence.

## Purpose

Protect factual and consequential execution after the plan is chosen or whenever uncertainty and impact require constrained behavior.

## Problem Solved

Exploratory reasoning can leak new assumptions, scope changes, or unsupported content into actions that require exact state, evidence, and authorization.

## Where It Fits in the OS

Roles: conservative execution mode, grounded commitment profile. Pipeline stages: execution readiness, atomic action, immediate verification, conservative finalization.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- source-faithful extraction
- production changes
- high-risk recommendations
- final publication
- irreversible operations

## When Not to Use

- the primary need is broad architecture discovery
- no plan or acceptance state has been committed
- the task is harmless creative exploration

## Scope

Canonical package: `safe-mode@1.1.0`. ID: `T4-06`. Functional classes: meta-control, truth-grounding. Activation: `U3-high-risk-expensive`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- execution is factual, consequential, or uncertain

## Non-Triggers

- the primary need is broad architecture discovery
- no plan or acceptance state has been committed
- the task is harmless creative exploration

## Inputs / Required State

- committed plan
- locked sources and state
- authorized action
- risk controls
- acceptance and rollback criteria

## Outputs / Produced State

- grounded bounded action
- atomic verification results
- updated verified state
- explicit blocker or conservative final output

## Mechanism

Lock the committed goal, sources, state version, authorized action, and acceptance criteria; narrow allowable drift to the requested execution delta. Before each consequential step verify its atomic prerequisites and authority, perform only that step, inspect the observable result, and stop on mismatch or missing evidence. SAFE does not mean low capability: it uses deep checks where risk demands, but it forbids speculative expansion during execution.

## Procedure

1. Declare SAFE and load the committed plan, authoritative state, permitted delta, and risk controls.
2. Verify prerequisites, permissions, evidence, and rollback before each consequential boundary.
3. Execute the smallest authorized action without reopening design alternatives.
4. Validate the immediate state change and protected invariants atomically.
5. Continue only on pass; otherwise stop, repair locally, or checkpoint for a supervised return to POWER.
6. Finalize conservatively with unresolved uncertainty and evidence limits visible.

## Always-Do Rules

- lock state and scope
- verify authority and prerequisites
- check each consequential result
- fail closed on unavailable required evidence

## Never-Do / Avoid Rules

- invent missing facts to complete execution
- broaden design inside an atomic action
- hide uncertainty for decisiveness
- treat SAFE as shallow or low-effort by definition

## Interaction Rules

### `critical-atomic-verification`

Atomic verification checks decisive claims and state changes before continuation.

### `grounding-no-invention`

Grounding blocks unsupported content during narrow execution.

### `hybrid-mode`

HYBRID provides the validated handoff from POWER planning into SAFE.

## Compatible Upgradeables

- `critical-atomic-verification` — Atomic verification checks decisive claims and state changes before continuation.
- `grounding-no-invention` — Grounding blocks unsupported content during narrow execution.
- `hybrid-mode` — HYBRID provides the validated handoff from POWER planning into SAFE.

## Counterbalancing Upgradeables

### `power-mode`

POWER reopens bounded design only when execution exposes a genuine architecture-level problem.

## Potential Redundancy

### `risk-tier-scaling`

Risk Tier selects mandatory rigor; SAFE is the concrete conservative execution profile.

### `grounding-no-invention`

Grounding is one invariant inside SAFE, not the entire mode.

## Conflict / Precedence Rules

- A missing required source, permission, or checkpoint blocks execution.
- Design changes discovered during SAFE are checkpointed and escalated rather than improvised.
- Urgency may narrow the action but cannot authorize unsupported facts or unavailable capabilities.

## Failure Boundary

- speculative execution
- silent scope expansion
- unverified state mutation
- false completion
- SAFE confused with minimal reasoning

## Strong-Model Scaling

May skip:

- repeating the mode label before every low-risk substep

Keep mandatory:

- scope and state lock
- atomic checks
- fail-closed evidence handling
- explicit replan boundary

## Recommended Skill Types

- high-stakes evidence work
- multi-step task execution
- skill and agent workflows
- source-grounded research

## Example Composition

**Task context:** Publish a validated repository after architecture is selected.

**Why it activates:** File changes and remote publication require exact state, credentials, and validation.

**Inputs/state:** The chosen plan, current Git state, test commands, repository name, and authenticated account are known.

**Action:** Applies only planned changes, verifies tests and diff, confirms remote target and visibility, publishes, and checks the public URL.

**Does not:** Invent credentials, redesign the repository during push, or claim publication before remote verification.

**Result/state change:** A grounded public release or a precise fail-closed blocker.

**Companions:** ['critical-atomic-verification', 'grounding-no-invention', 'hybrid-mode']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-06` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 10. Tier-4 / Meta-Supervisor recovered family (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 17. VERBATIM-COPY / FIDELITY WORKFLOW — EXAMPLE OF UPGRADEABLE COMPOSITION (historical_assistant_artifact)
