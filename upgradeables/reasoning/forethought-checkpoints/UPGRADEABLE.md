# Forethought / Checkpoints

## Summary

Places predictive checks immediately before costly, irreversible, or dependency-sensitive actions.

## Purpose

Catch missing prerequisites and foreseeable downstream failure while reversal is still cheap.

## Problem Solved

A locally valid next step can commit the workflow to an expensive path whose dependencies, blast radius, or rollback conditions were never checked.

## Where It Fits in the OS

Roles: pre-commit control, risk checkpoint. Pipeline stages: before external action, before destructive change, before dependency handoff.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- deployments
- schema or API changes
- financial or external communications
- multi-stage automation

## When Not to Use

- reversible low-cost local edits
- the checkpoint would duplicate an already enforced transaction guard
- urgent containment requires a preauthorized emergency procedure

## Scope

Canonical package: `forethought-checkpoints@1.1.0`. ID: `T2-17`. Functional classes: planning-reasoning, validation. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- an action is costly, irreversible, or dependency-sensitive

## Non-Triggers

- reversible low-cost local edits
- the checkpoint would duplicate an already enforced transaction guard
- urgent containment requires a preauthorized emergency procedure

## Inputs / Required State

- planned action
- dependencies
- risk tier
- prerequisites
- rollback capability

## Outputs / Produced State

- checkpoint decision
- predicted failure
- verified prerequisites
- post-action observation

## Mechanism

At each consequential boundary, predict the most likely downstream failure, verify the prerequisite that would prevent it, define observable success and rollback, then commit and check the result. Checkpoints are placed by consequence rather than at every trivial step.

## Procedure

1. Identify the next irreversible, high-cost, or dependency-sensitive action.
2. Name the plausible downstream failure and affected dependency.
3. Verify prerequisites, authority, backups, and rollback path proportionate to risk.
4. Define the immediate post-action observation that indicates success or failure.
5. Commit only if the checkpoint passes, then inspect the result before continuing.

## Always-Do Rules

- tie each checkpoint to a concrete consequence
- verify prerequisite before commitment
- define post-commit observation

## Never-Do / Avoid Rules

- turn every minor step into ceremonial review
- treat a prediction as verified fact
- continue past a failed prerequisite without escalation

## Interaction Rules

### `risk-tier-scaling`

Risk Tier Scaling determines how deep the checkpoint must be.

### `bounded-exit`

Bounded ExIt prevents repeated checkpoint analysis once required evidence and safeguards are sufficient.

## Compatible Upgradeables

- `risk-tier-scaling` — Risk Tier Scaling determines how deep the checkpoint must be.
- `bounded-exit` — Bounded ExIt prevents repeated checkpoint analysis once required evidence and safeguards are sufficient.

## Counterbalancing Upgradeables

### `reasoning-scale-controller`

Proportionality keeps checkpoint overhead aligned to actual consequence.

## Potential Redundancy

### `risk-tier-scaling`

Risk tier sets rigor globally; Forethought performs the concrete pre-commit prediction and prerequisite check.

## Conflict / Precedence Rules

- A failed hard prerequisite blocks commitment regardless of schedule pressure.
- During urgent containment, use the approved emergency checkpoint rather than omitting checks entirely.

## Failure Boundary

- ritual checklists unrelated to risk
- analysis after commitment instead of before
- missing rollback for destructive action
- unchecked dependency assumptions

## Strong-Model Scaling

May skip:

- explicit checkpoint prose for a fully reversible in-memory operation

Keep mandatory:

- pre-commit prerequisite check for consequential actions
- success and rollback observation

## Recommended Skill Types

- analysis and decision support
- high-stakes evidence work
- review and quality assurance
- structured problem solving

## Example Composition

**Task context:** Rename a production API field.

**Why it activates:** The change can break downstream consumers and is costly to reverse after rollout.

**Inputs/state:** Consumer inventory, compatibility plan, telemetry, and rollback deployment exist.

**Action:** Verifies consumer migration, stages compatibility, sets an error-rate threshold, deploys, and checks telemetry before removing the old field.

**Does not:** Approve the rename because the local service tests pass.

**Result/state change:** A gated rollout with evidence before irreversible cleanup.

**Companions:** ['risk-tier-scaling', 'multi-layer-consistency']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-17` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 1. Canonical current consolidated inventory (historical_recovery_inventory)
