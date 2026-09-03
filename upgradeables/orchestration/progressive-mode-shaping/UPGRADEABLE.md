# Progressive Mode Shaping

## Summary

Narrow a broad exploratory workflow through comparison and selection into precise execution as decisions become locked.

## Purpose

Narrow a broad exploratory workflow through comparison and selection into precise execution as decisions become locked.

## Problem Solved

A task can remain indefinitely exploratory or switch abruptly into execution while discarded possibilities still influence active state.

## Where It Fits in the OS

Roles: mode transition control, commitment shaping. Pipeline stages: exploration, candidate comparison, decision lock, execution handoff.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- design-to-implementation workflows
- iterative planning
- creative work with a committed deliverable

## When Not to Use

- the task is purely exploratory and requires no commitment
- the task begins with one already locked deterministic procedure

## Scope

Canonical package: `progressive-mode-shaping@1.1.0`. ID: `T2-06`. Functional classes: orchestration, planning-reasoning. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- work moves from design to execution

## Non-Triggers

- the task is purely exploratory and requires no commitment
- the task begins with one already locked deterministic procedure

## Inputs / Required State

- current phase and open decisions
- candidate set and comparison evidence
- locked constraints and transition criteria

## Outputs / Produced State

- narrowed active mode
- retired alternatives and locked execution plan

## Mechanism

Track which choices remain open and progressively reduce permitted breadth as evidence and decisions accumulate. Move through explore, compare, choose, plan, execute, and validate states; at each transition retire losing branches, lock accepted constraints, and lower drift. Unlike a hard two-mode switch, shaping may narrow in several evidence-backed increments.

## Procedure

1. Declare the initial exploration boundary and the decisions that must eventually lock.
2. Generate only the breadth justified at the current phase.
3. Compare candidates and record evidence for accepted and rejected choices.
4. Lock decisions and reduce allowed alternatives and drift at each phase transition.
5. Enter execution with one active plan, then validate against the locked state.

## Always-Do Rules

- Preserve the defining invariant: evidence-backed narrowing and retirement of losing branches before execution.
- Record material routing, transition, and failure decisions in explicit task state.

## Never-Do / Avoid Rules

- keeping every alternative active through execution or narrowing without evidence
- Never claim hidden state, unavailable host capability, or authority beyond the active Skill.

## Interaction Rules

### `stateblock`

Records phase, decisions, active branches, and transition evidence.

### `mode-lock-in`

Prevents a completed transition from silently reopening discarded modes.

## Compatible Upgradeables

- `stateblock` — Records phase, decisions, active branches, and transition evidence.
- `mode-lock-in` — Prevents a completed transition from silently reopening discarded modes.

## Counterbalancing Upgradeables

### `anti-tunnel-vision`

Ensures early narrowing does not occur before a plausible alternative is considered.

## Potential Redundancy

### `hybrid-mode`

HYBRID uses a distinct POWER-to-SAFE gate; Progressive Mode Shaping supports multiple gradual narrowing transitions.

## Conflict / Precedence Rules

- Host, system, domain, and explicit user authority take precedence over this component.
- If transition criteria are absent or accepted decisions cannot be distinguished from open options, stop or escalate rather than forcing a nominal success.

## Failure Boundary

- transition criteria are absent or accepted decisions cannot be distinguished from open options
- narrowing would discard a materially plausible path before comparison

## Strong-Model Scaling

May skip:

- intermediate shaping stages for a trivial two-step task

Keep mandatory:

- evidence-backed narrowing and retirement of losing branches before execution

## Recommended Skill Types

- analysis and decision support
- communication and content generation
- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** A product team moves from broad feature concepts to one implementation specification.

**Why it activates:** Exploration is useful early but must not persist into engineering execution.

**Inputs/state:** Candidate features, criteria, decisions, constraints, and current phase.

**Action:** Narrows from ideation to comparison to one plan, locking decisions at each transition.

**Does not:** Does not keep rejected features active or force a premature choice without comparison.

**Result/state change:** Engineering receives one precise specification with traceable retired alternatives.

**Companions:** StateBlock records locks; Anti-Tunnel Vision protects early comparison.

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-06` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
