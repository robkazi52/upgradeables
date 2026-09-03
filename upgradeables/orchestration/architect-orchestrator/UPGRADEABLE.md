# Architect Orchestrator

## Summary

Plan and coordinate modular system design from goal discovery through critique, localized repair, synthesis, and continuation state.

## Purpose

Plan and coordinate modular system design from goal discovery through critique, localized repair, synthesis, and continuation state.

## Problem Solved

Complex architecture work fails when planning, component selection, execution, critique, and state handoff occur without one explicit modular workflow.

## Where It Fits in the OS

Roles: architecture orchestration, task-level coordination. Pipeline stages: intake and framing, modular planning, execution coordination, critique and synthesis, state handoff.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- Skill and OS architecture
- workflow design
- framework refactoring

## When Not to Use

- the task is a narrow domain execution job with no architecture decision
- a single existing component already performs the complete bounded task

## Scope

Canonical package: `architect-orchestrator@1.1.0`. ID: `O-01`. Functional classes: orchestration, meta-control, planning-reasoning. Activation: `U4-meta-architecture`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- designing or refactoring a Skill, OS, framework, or workflow

## Non-Triggers

- the task is a narrow domain execution job with no architecture decision
- a single existing component already performs the complete bounded task

## Inputs / Required State

- locked architecture goal and constraints
- available component manifests and interfaces
- authority and completion criteria

## Outputs / Produced State

- modular architecture and execution plan
- critiqued synthesis with compact continuation state

## Mechanism

Translate the locked goal and constraints into a modular plan, select only the necessary OS layers, Genes, Cores, Upgradeables, references, and validators, then coordinate their ordered execution. After execution, run a separate critique, route localized defects to bounded repair, synthesize one result, and emit the minimum continuation state. The orchestrator owns coordination, not every domain operation.

## Procedure

1. Lock the goal, constraints, deliverable, authority, and completion criteria.
2. Decompose the architecture into modules with explicit interfaces and dependencies.
3. Select the minimum required components and resolve authority, conflict, and load order.
4. Coordinate execution or delegation while passing only explicit bounded state.
5. Critique the assembled result, apply localized repair, synthesize, and emit a compact state snapshot.

## Always-Do Rules

- Preserve the defining invariant: explicit modular interfaces, authority resolution, independent critique, and continuation state.
- Record material routing, transition, and failure decisions in explicit task state.

## Never-Do / Avoid Rules

- returning a flat component list or impersonating the domain execution agent
- Never claim hidden state, unavailable host capability, or authority beyond the active Skill.

## Interaction Rules

### `scoped-loader`

Activates only the modules selected by the architecture plan.

### `state-snapshot`

Captures the goal, locked decisions, active modules, open issues, and next step after synthesis.

## Compatible Upgradeables

- `scoped-loader` — Activates only the modules selected by the architecture plan.
- `state-snapshot` — Captures the goal, locked decisions, active modules, open issues, and next step after synthesis.

## Counterbalancing Upgradeables

### `cognitive-governor`

Bounds architectural exploration and prevents orchestration from becoming endless redesign.

## Potential Redundancy

### `ultimate-suite-supervisor`

The suite supervisor governs modes and pack health in an existing full OS; Architect Orchestrator designs and coordinates the task architecture itself.

## Conflict / Precedence Rules

- Host, system, domain, and explicit user authority take precedence over this component.
- If required module interfaces or authority relationships cannot be resolved, stop or escalate rather than forcing a nominal success.

## Failure Boundary

- required module interfaces or authority relationships cannot be resolved
- the requested work is domain execution outside the orchestrator's design scope

## Strong-Model Scaling

May skip:

- verbose role-by-role narration when one agent can execute the modular plan directly

Keep mandatory:

- explicit modular interfaces, authority resolution, independent critique, and continuation state

## Recommended Skill Types

- Skill and OS architecture
- workflow design
- framework refactoring

## Example Composition

**Task context:** A team needs a portable research Skill with retrieval, state, grounding, and citation checks.

**Why it activates:** The task requires component architecture and a validated complete package, not one isolated primitive.

**Inputs/state:** Skill goal, provider constraints, registry manifests, tests, and output contract.

**Action:** Builds a modular plan, selects components, coordinates drafting and critique, repairs local defects, and emits the finished Skill plus state.

**Does not:** Does not act as the research domain expert or load every available component.

**Result/state change:** A minimal coherent Skill and a compact record of decisions are produced.

**Companions:** Scoped Loader activates selected modules; State Snapshot preserves the handoff.

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `O-01` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — O-01. Architect Orchestrator (current_consolidated_catalog)
