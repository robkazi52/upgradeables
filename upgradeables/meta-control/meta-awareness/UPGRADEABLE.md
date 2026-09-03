# Meta-Awareness Pack

## Summary

Observes active modes, reasoning health, state, and module interactions for task-process failure without making identity or consciousness claims.

## Purpose

Turn process-health signals into explicit observations that a supervisor can route to repair, pause, or continuation.

## Problem Solved

Complex scaffolding can fail through mode mismatch, stale state, loops, contradiction, or module conflict while the produced content still appears fluent.

## Where It Fits in the OS

Roles: process-health sensor, meta-control observer. Pipeline stages: runtime observation, health classification, supervisor notification.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- long multi-module workflows
- multi-agent coordination
- iterative reasoning
- mode-rich systems

## When Not to Use

- a simple task has no meaningful process state
- the requested analysis concerns sentience or identity rather than task-process health
- monitoring cannot observe the claimed signal

## Scope

Canonical package: `meta-awareness@1.1.0`. ID: `T4-02`. Functional classes: meta-control, validation. Activation: `U4-meta-architecture`. Mechanism basis: `normalized-from-recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- process failure signals must be observed

## Non-Triggers

- a simple task has no meaningful process state
- the requested analysis concerns sentience or identity rather than task-process health
- monitoring cannot observe the claimed signal

## Inputs / Required State

- declared mode
- locked goal and state version
- active module map
- progress and repetition signals
- health thresholds

## Outputs / Produced State

- pass
- fail
- repair-required
- unverifiable
- evidence-backed health observation

## Mechanism

Maintain a small observable health frame: declared mode, current goal and state version, active modules, progress signal, repeated action signature, unresolved contradictions, and authority conflicts. Compare these observations with expected workflow state at checkpoints and emit pass, fail, repair-required, or unverifiable plus evidence; the pack diagnoses and reports but does not silently reroute or rewrite the task.

## Procedure

1. Read declared mode, locked goal, state version, active modules, and expected next transition.
2. Collect observable indicators of progress, repetition, contradiction, state staleness, and module conflict.
3. Compare indicators with thresholds and workflow expectations.
4. Classify health as pass, fail, repair-required, or unverifiable and attach the triggering evidence.
5. Send the finding to Meta-Supervisor or the owning workflow without changing authority or inventing internal mental-state explanations.

## Always-Do Rules

- limit claims to observable process state
- attach evidence to a health finding
- distinguish detection from repair
- emit unverifiable when a signal cannot be checked

## Never-Do / Avoid Rules

- claim consciousness, identity, hidden intention, or latent state
- silently change the active mode
- certify health from fluent output alone
- diagnose unavailable internal processes

## Interaction Rules

### `meta-supervisor`

Meta-Supervisor consumes health findings and chooses the appropriate repair or routing action.

### `stuck-pattern-reset`

A repeated-action finding can activate the bounded reset pack.

### `contradiction-micro-repair`

A localized contradiction finding can route to targeted repair.

## Compatible Upgradeables

- `meta-supervisor` — Meta-Supervisor consumes health findings and chooses the appropriate repair or routing action.
- `stuck-pattern-reset` — A repeated-action finding can activate the bounded reset pack.
- `contradiction-micro-repair` — A localized contradiction finding can route to targeted repair.

## Counterbalancing Upgradeables

### `reasoning-throughput-governor`

Throughput limits monitoring overhead so observation does not dominate task work.

## Potential Redundancy

### `meta-supervisor`

Meta-Awareness senses and classifies; Meta-Supervisor decides and routes.

### `coherence-heartbeat`

Heartbeat checks global plan/state/output coherence; Meta-Awareness additionally observes modes, loops, and module interactions.

## Conflict / Precedence Rules

- An unverifiable signal cannot be reported as a failure or a pass.
- Observed authority conflict is surfaced to the supervisor, not resolved by the sensor.
- Safety-critical failure may trigger a predeclared pause but still requires explicit routing.

## Failure Boundary

- anthropomorphic narratives
- unobservable-state claims
- monitoring without evidence
- sensor taking supervisor authority
- monitoring overload

## Strong-Model Scaling

May skip:

- visible health snapshots at every trivial step

Keep mandatory:

- observable-only claims
- mode and state checks at consequential transitions
- evidence-bearing status

## Recommended Skill Types

- long multi-module workflows
- multi-agent coordination
- iterative reasoning
- mode-rich systems

## Example Composition

**Task context:** A multi-agent build repeats validation without changing the failing files.

**Why it activates:** The process may be stuck even though each agent reports activity.

**Inputs/state:** Command logs, state versions, active-agent tasks, and the same recurring error are observable.

**Action:** Detects unchanged state and repeated action signatures, emits repair-required with evidence, and routes the finding to Meta-Supervisor.

**Does not:** Claim the agents are confused or reset their work directly.

**Result/state change:** A grounded process-health diagnosis ready for supervisor action.

**Companions:** ['meta-supervisor', 'stuck-pattern-reset']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-02` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T4-02. Meta-Awareness Pack (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 10. Tier-4 / Meta-Supervisor recovered family (historical_recovery_inventory)
