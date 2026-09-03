# Conservative Execution Mode (`safe-mode@1.1.0`)

Recovered name: SAFE Mode

Purpose: Protect factual and consequential execution after the plan is chosen or whenever uncertainty and impact require constrained behavior.

Activate when: execution is factual, consequential, or uncertain.

Do not use when: the primary need is broad architecture discovery; no plan or acceptance state has been committed.

Requires: none.

## Runtime mechanism

Lock the committed goal, sources, state version, authorized action, and acceptance criteria; narrow allowable drift to the requested execution delta. Before each consequential step verify its atomic prerequisites and authority, perform only that step, inspect the observable result, and stop on mismatch or missing evidence. SAFE does not mean low capability: it uses deep checks where risk demands, but it forbids speculative expansion during execution.

## Procedure

1. Declare SAFE and load the committed plan, authoritative state, permitted delta, and risk controls.
2. Verify prerequisites, permissions, evidence, and rollback before each consequential boundary.
3. Execute the smallest authorized action without reopening design alternatives.
4. Validate the immediate state change and protected invariants atomically.
5. Continue only on pass; otherwise stop, repair locally, or checkpoint for a supervised return to POWER.

## Guardrails

- Mandatory even on strong models: scope and state lock; atomic checks; fail-closed evidence handling.
- Conflict/precedence: A missing required source, permission, or checkpoint blocks execution; Design changes discovered during SAFE are checkpointed and escalated rather than improvised.
- Stop or fail when: speculative execution; silent scope expansion.

Full package and provenance: [`safe-mode`](../../upgradeables/meta-control/safe-mode/UPGRADEABLE.md).
