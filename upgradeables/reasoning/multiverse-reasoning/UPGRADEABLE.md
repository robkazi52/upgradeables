# Multiverse Engine

## Summary

Creates two or three materially different solution worlds, evaluates each against one shared rubric, and commits to one result while retiring the rest.

## Purpose

Obtain real alternative search without losing control of truth, constraints, cost, or convergence.

## Problem Solved

A single-path solver can overfit its first plan; an unconstrained multi-agent or brainstorming process can instead proliferate branches without a defensible collapse.

## Where It Fits in the OS

Roles: bounded parallel reasoning engine, candidate selection controller. Pipeline stages: planning, hypothesis comparison, architecture selection, pre-draft outline selection.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- ambiguous design choices
- research plans
- narrative or document architectures
- competing causal models

## When Not to Use

- a locked source dictates a single faithful transformation
- one hard constraint eliminates all but one path
- the task is too small for branch overhead

## Scope

Canonical package: `multiverse-reasoning@1.1.0`. ID: `A-01`. Functional classes: planning-reasoning. Activation: `U3-high-risk-expensive`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- competing hypotheses or designs would add value

## Non-Triggers

- a locked source dictates a single faithful transformation
- one hard constraint eliminates all but one path
- the task is too small for branch overhead

## Inputs / Required State

- locked task state
- shared evidence
- branch budget
- common evaluation rubric
- hard vetoes

## Outputs / Produced State

- two or three branch records
- cross-branch evaluation
- selected or synthesized plan
- retirement record

## Mechanism

Open exactly two or three branch records that differ in strategy, causal model, or architecture. Give every branch the same locked facts, requirements, risk limits, and evaluation rubric; develop each only far enough to expose its decisive tradeoffs. Score them, apply hard vetoes before soft preferences, select or synthesize one committed path, and mark every losing branch retired so its assumptions cannot leak into execution.

## Procedure

1. Lock shared facts, goals, constraints, risk boundaries, and a branch budget of two or three.
2. Define branches with a one-sentence strategy, distinctive assumption, predicted advantage, and disconfirming condition.
3. Develop each branch to the same decision depth; do not let the favored branch consume the entire budget.
4. Evaluate all branches on the same dimensions, such as truth, requirement coverage, coherence, cost, risk, and reversibility.
5. Veto any branch that violates a hard constraint, then select the strongest survivor or synthesize only compatible components.
6. Emit one committed plan plus a retirement record naming rejected branches and why they must not influence downstream work.

## Always-Do Rules

- make branches materially distinct
- use a common rubric
- apply hard constraints before aggregate scores
- retire losing branches explicitly

## Never-Do / Avoid Rules

- create unbounded universes
- score one branch on easier criteria
- blend mutually inconsistent assumptions during synthesis
- carry losing-branch instructions into the chosen execution state

## Interaction Rules

### `parallel-qms`

Parallel-QMS provides the shared multidimensional scoring and collapse gate.

### `anti-tunnel-vision`

Anti-Tunnel Vision audits whether branch diversity is real and whether the favorite was preselected.

### `task-set-lock-in`

Task-Set Lock-In gives all branches identical goals and non-negotiable constraints.

## Compatible Upgradeables

- `parallel-qms` — Parallel-QMS provides the shared multidimensional scoring and collapse gate.
- `anti-tunnel-vision` — Anti-Tunnel Vision audits whether branch diversity is real and whether the favorite was preselected.
- `task-set-lock-in` — Task-Set Lock-In gives all branches identical goals and non-negotiable constraints.

## Counterbalancing Upgradeables

### `bounded-exit`

Bounded ExIt prevents branch development or comparison from continuing after the decision value falls below cost.

### `neuro-focus`

After collapse, Neuro-Focus narrows execution to the selected universe.

## Potential Redundancy

### `anti-tunnel-vision`

Both counter first-path fixation; Multiverse manages full candidate state and collapse, while Anti-Tunnel can be a lighter rival check.

### `parallel-qms`

QMS evaluates alternatives but does not itself generate or retire branch worlds.

## Conflict / Precedence Rules

- A hard truth, safety, or authorization veto cannot be outvoted by soft quality scores.
- Synthesis is allowed only when selected components share compatible assumptions and interfaces.
- If no branch passes, return the blocking constraint or request evidence rather than select the least-invalid branch.

## Failure Boundary

- cosmetic branch variants
- unbounded branching
- unequal evaluation depth
- majority voting over a hard veto
- assumption leakage from retired branches

## Strong-Model Scaling

May skip:

- separate long-form prose for every branch when compact branch records expose the tradeoffs

Keep mandatory:

- material branch distinctness
- shared rubric
- hard-veto precedence
- explicit collapse and retirement

## Recommended Skill Types

- ambiguous design choices
- research plans
- narrative or document architectures
- competing causal models

## Example Composition

**Task context:** Design a community skill repository contribution model.

**Why it activates:** Central curation, open pull requests, and federated registries have materially different trust and maintenance tradeoffs.

**Inputs/state:** Public accessibility, vendor neutrality, provenance, and low maintainer burden are locked criteria.

**Action:** Builds three compact branch records, evaluates each against the same governance and usability rubric, vetoes the federation branch if discoverability cannot be guaranteed, and selects an open-PR model with automated validation.

**Does not:** Call three slightly different pull-request workflows separate universes or retain federation-only assumptions in the chosen plan.

**Result/state change:** One executable governance plan with two retired alternatives and explicit reasons.

**Companions:** ['parallel-qms', 'anti-tunnel-vision', 'task-set-lock-in']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `A-01` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — A-01. Multiverse Engine (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 11. Advanced architecture Upgradeables retained (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.4 Multiverse / plan generation (historical_assistant_artifact)
