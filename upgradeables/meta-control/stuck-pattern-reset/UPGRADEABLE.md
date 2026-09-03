# Stuck-Pattern Reset Pack

## Summary

Detects repeated failed reasoning and abandons only that path while preserving locked facts, constraints, accepted work, and explicit state.

## Purpose

Break nonproductive loops without erasing the trustworthy task context needed for a genuinely different next attempt.

## Problem Solved

A solver can repeat the same search, edit, tool call, or reasoning pattern with superficial variations, consuming budget without changing the blocking condition.

## Where It Fits in the OS

Roles: loop-break repair pack, failed-path reset controller. Pipeline stages: repetition detection, state preservation, path quarantine, alternative restart.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- repeated tool failures
- recursive revision loops
- stale debugging hypotheses
- nonconverging planning

## When Not to Use

- a second attempt has new evidence or a materially changed method
- the whole task state is corrupted
- a mandatory retry protocol has not been exhausted

## Scope

Canonical package: `stuck-pattern-reset@1.1.0`. ID: `T4-03`. Functional classes: meta-control, editing-repair. Activation: `U2-specialized`. Mechanism basis: `recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- reasoning loops or stale approaches repeat

## Non-Triggers

- a second attempt has new evidence or a materially changed method
- the whole task state is corrupted
- a mandatory retry protocol has not been exhausted

## Inputs / Required State

- attempt history
- state versions
- locked facts and constraints
- observed failures
- alternative methods and retry limit

## Outputs / Produced State

- stuck-pattern determination
- preserved-state snapshot
- quarantined path
- materially different next attempt or escalation

## Mechanism

Fingerprint attempts by goal, assumptions, method, inputs, and failure result rather than wording. When a predeclared repetition threshold is met without new evidence or state change, snapshot locked facts and accepted results, quarantine the failed path and its unsupported assumptions, state the recurring blocker, and restart from a materially different method or escalate. Only the failed reasoning path resets.

## Procedure

1. Record each attempt's goal, method, key assumptions, state version, and observed failure.
2. Compare the new attempt with prior fingerprints and test whether evidence, inputs, or method materially changed.
3. On repeated failure, freeze locked facts, constraints, accepted outputs, and unresolved evidence.
4. Quarantine the failed path and name the blocker it could not overcome.
5. Choose a different hypothesis, tool, decomposition, or escalation route with a new success test.
6. Run one bounded attempt and recheck; escalate if the same blocker persists.

## Always-Do Rules

- detect semantic repetition rather than repeated wording
- preserve trusted state
- make the replacement path materially different
- set a bounded retry limit

## Never-Do / Avoid Rules

- reset facts or user constraints
- call normal iteration stuckness
- retry with cosmetic prompt changes
- erase failure evidence that should inform the next path

## Interaction Rules

### `bounded-exit`

Bounded ExIt supplies the threshold for stopping low-value repeated passes.

### `stateblock`

StateBlock preserves the trustworthy context before the path is reset.

### `meta-supervisor`

Meta-Supervisor validates the stuck diagnosis and routes the reset.

## Compatible Upgradeables

- `bounded-exit` — Bounded ExIt supplies the threshold for stopping low-value repeated passes.
- `stateblock` — StateBlock preserves the trustworthy context before the path is reset.
- `meta-supervisor` — Meta-Supervisor validates the stuck diagnosis and routes the reset.

## Counterbalancing Upgradeables

### `forethought-checkpoints`

Forethought prevents the alternative restart from repeating the same costly commitment without a new prerequisite.

## Potential Redundancy

### `meta-stability`

Reset isolates one failed path; Meta-Stability reconciles broader state and module instability.

### `anti-tunnel-vision`

Anti-Tunnel prevents early fixation; Stuck Reset acts after repetition proves fixation persistent.

## Conflict / Precedence Rules

- Locked facts and constraints survive the reset.
- If every materially distinct path shares the same external blocker, escalate rather than keep resetting.
- A destructive alternative requires its own pre-commit authorization.

## Failure Boundary

- false loop detection
- full-context amnesia
- cosmetic retries
- unbounded reset cycle
- destructive alternative without checkpoint

## Strong-Model Scaling

May skip:

- formal fingerprints when two attempts are obviously identical and logged

Keep mandatory:

- trusted-state preservation
- material-difference test
- retry bound
- external-blocker escalation

## Recommended Skill Types

- document and code transformation
- multi-step task execution
- review and quality assurance
- skill and agent workflows

## Example Composition

**Task context:** Three searches use rephrased queries but return the same irrelevant repository results.

**Why it activates:** The method and corpus are unchanged despite different wording.

**Inputs/state:** Query logs, target identifiers, accepted facts, and local source files are available.

**Action:** Preserves the target and findings, quarantines web query reformulation, switches to identifier search inside the local archive, and sets one success check.

**Does not:** Forget the verified target or issue a fourth cosmetic query.

**Result/state change:** A materially different recovery path or an explicit source blocker.

**Companions:** ['bounded-exit', 'stateblock', 'meta-supervisor']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-03` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 10. Tier-4 / Meta-Supervisor recovered family (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 9. BOUNDED EXIT — DEEPER HISTORICAL USE (historical_assistant_artifact)
