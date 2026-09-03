# Work Reflection Loop OS / ReflectOS

## Summary

The Work Reflection Loop OS: a bounded, goal-anchored reflect-test-revise loop that chooses accept, revise, or permitted escalation and then updates task state.

## Purpose

Correct process and output errors at meaningful checkpoints without turning reflection into unbounded rumination or invented content.

## Problem Solved

Work can continue after requirements, contradictions, missing items, or risk have changed, while generic self-critique tends to loop or generate unsupported improvements.

## Where It Fits in the OS

Roles: goal-anchored-work-reflection, bounded-qa-controller, state-update-trigger. Pipeline stages: milestone review, pre-delivery, after failed validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-step implementation
- research synthesis
- document revision
- agent handoffs
- recovery after test failure

## When Not to Use

- a deterministic fix is already known and reflection adds no decision value
- the caller asks for unconstrained ideation rather than requirement checking

## Scope

Canonical package: `reflectos@1.1.0`. ID: `T2-12`. Functional classes: validation, editing-repair. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- output needs a deliberate quality pass

## Non-Triggers

- a deterministic fix is already known and reflection adds no decision value
- the caller asks for unconstrained ideation rather than requirement checking

## Inputs / Required State

- session goal
- current subgoal
- requirements
- current output
- test evidence
- risk signals
- StateBlock

## Outputs / Produced State

- accept/revise/escalate decision
- requirement-linked corrections
- updated StateBlock
- stop reason

## Mechanism

At a bounded checkpoint, re-read the session goal and current subgoal, compare the actual output to explicit requirements, audit contradictions, omissions, and risk, then select exactly one transition: accept, revise, or ask/escalate where permitted. After the transition, update the StateBlock to reflect task reality; reflection may correct process errors but may not invent facts or construct an identity narrative.

## Procedure

1. Recheck the session goal and current subgoal.
2. Compare the produced artifact or action with every explicit requirement.
3. Audit contradictions, missing requirements, failed evidence, and material risk.
4. Choose accept, revise, or ask/escalate when permitted.
5. If revising, make the smallest requirement-linked correction and retest.
6. Stop on acceptance, external dependency, or the declared loop budget.
7. Update StateBlock with actual progress, decisions, remaining work, and evidence.

## Always-Do Rules

- Anchor every critique to the goal, requirements, or observed risk.
- Choose an explicit loop transition.
- Update task state after the decision.
- Use a bounded iteration budget.

## Never-Do / Avoid Rules

- Invent facts to make the output appear complete.
- Reflect indefinitely without new evidence or a changed action.
- Build an identity or self-story in StateBlock.
- Expand scope merely because reflection found optional improvements.

## Interaction Rules

### `stateblock`

Receives the updated factual work state after each loop decision.

### `bounded-exit`

Enforces stop conditions on revise cycles.

### `coherence-loops`

Handles broader cross-artifact inconsistencies identified during the audit.

## Compatible Upgradeables

- `stateblock` — Receives the updated factual work state after each loop decision.
- `bounded-exit` — Enforces stop conditions on revise cycles.
- `coherence-loops` — Handles broader cross-artifact inconsistencies identified during the audit.

## Counterbalancing Upgradeables

### `crispr-edit`

Restricts revisions to requirement-linked corrections.

## Potential Redundancy

### `coherence-loops`

ReflectOS decides whether work should be accepted, revised, or escalated; coherence loops specifically repair systemic inconsistency.

## Conflict / Precedence Rules

- Explicit requirements and evidence outrank the reflector's preference.
- When a missing fact cannot be recovered, escalate or qualify rather than fabricate.
- A fixed loop budget stops revision but does not convert failure into acceptance.

## Failure Boundary

- Do not accept when a material requirement is unmet; do not revise with invented facts; stop and surface the dependency when progress requires external authority.

## Strong-Model Scaling

May skip:

- formal reflection on a trivial already-verified operation

Keep mandatory:

- goal comparison, requirement audit, explicit transition, and state update for long or risky work

## Recommended Skill Types

- multi-step implementation
- research synthesis
- document revision
- agent handoffs
- recovery after test failure

## Example Composition

**Task context:** A repository build reaches pre-release after generating many packages.

**Why it activates:** Completion requires more than generation: schemas, tests, docs, Git, and publication must match the handoff.

**Inputs/state:** Build specification, generated tree, validation output, and current StateBlock.

**Action:** Finds a missing all-package validation path, selects revise, adds the relevant test, reruns checks, then accepts and updates state.

**Does not:** Declare success because scaffolding exists or invent a passing publication result.

**Result/state change:** The release decision is tied to requirements and evidence with a bounded repair history.

**Companions:** ['stateblock', 'bounded-exit', 'coherence-loops']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-12` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: WRL, ReflectOS.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T2-12. WRL / ReflectOS (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — T2-12. WRL / ReflectOS (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — bounded WRL / ReflectOS (historical_assistant_artifact)
