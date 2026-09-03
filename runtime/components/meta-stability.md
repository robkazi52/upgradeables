# Stable-State Recovery Mode (`meta-stability@1.1.0`)

Recovered name: Meta-Stability Mode

Purpose: Preserve a trusted task state while isolating drift sources and resuming from one explicit authority-consistent configuration.

Activate when: coherence degrades under repeated change.

Do not use when: one local defect can be repaired directly; the trusted checkpoint is itself invalid.

Requires: none.

## Runtime mechanism

On a defined instability signal, freeze optional activations and structural changes, select the latest verified state snapshot, and compare active goals, modules, decisions, and open issues against that checkpoint. Quarantine conflicting deltas, re-establish one authority order and next step, run a coherence check, then resume changes one at a time with observation; MSM stabilizes state, not content by force.

## Procedure

1. Confirm an instability trigger such as state divergence, repeated regression, or unresolved module conflict.
2. Pause optional changes and capture the current state without overwriting the last verified checkpoint.
3. Compare goals, decisions, modules, sources, and open issues with the verified snapshot.
4. Quarantine unverified deltas and resolve authority conflicts explicitly.
5. Run coherence, state-version, and invariant checks on the restored configuration.

## Guardrails

- Mandatory even on strong models: verified checkpoint; optional-change freeze; authority reconciliation.
- Conflict/precedence: A user-approved newer decision is not rolled back solely because an older checkpoint is internally coherent; Urgent safety containment may proceed through a predeclared minimal path while optional work remains frozen.
- Stop or fail when: stability theater; loss of newer valid state.

Full package and provenance: [`meta-stability`](../../upgradeables/meta-control/meta-stability/UPGRADEABLE.md).
