# Stuck-Pattern Reset Pack (`stuck-pattern-reset@1.1.0`)

Purpose: Break nonproductive loops without erasing the trustworthy task context needed for a genuinely different next attempt.

Activate when: reasoning loops or stale approaches repeat.

Do not use when: a second attempt has new evidence or a materially changed method; the whole task state is corrupted.

Requires: none.

## Runtime mechanism

Fingerprint attempts by goal, assumptions, method, inputs, and failure result rather than wording. When a predeclared repetition threshold is met without new evidence or state change, snapshot locked facts and accepted results, quarantine the failed path and its unsupported assumptions, state the recurring blocker, and restart from a materially different method or escalate. Only the failed reasoning path resets.

## Procedure

1. Record each attempt's goal, method, key assumptions, state version, and observed failure.
2. Compare the new attempt with prior fingerprints and test whether evidence, inputs, or method materially changed.
3. On repeated failure, freeze locked facts, constraints, accepted outputs, and unresolved evidence.
4. Quarantine the failed path and name the blocker it could not overcome.
5. Choose a different hypothesis, tool, decomposition, or escalation route with a new success test.

## Guardrails

- Mandatory even on strong models: trusted-state preservation; material-difference test; retry bound.
- Conflict/precedence: Locked facts and constraints survive the reset; If every materially distinct path shares the same external blocker, escalate rather than keep resetting.
- Stop or fail when: false loop detection; full-context amnesia.

Full package and provenance: [`stuck-pattern-reset`](../../upgradeables/meta-control/stuck-pattern-reset/UPGRADEABLE.md).
