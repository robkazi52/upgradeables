# Bounded Iteration Stop Rule (`bounded-exit@1.1.0`)

Recovered name: Bounded ExIt

Purpose: Turn iterative improvement into a terminating control loop with explicit quality, budget, and diminishing-return gates.

Activate when: a draft needs iterative improvement.

Do not use when: a mandatory validator has not yet passed; a hard defect requires escalation rather than iteration.

Requires: none.

## Runtime mechanism

Each pass evaluates the artifact against locked goals, chooses the single highest-value remaining defect, repairs it, and re-evaluates. Exit occurs on threshold satisfaction, budget exhaustion, or diminishing expected improvement; the historical acronym expansion is deliberately left unrecovered.

## Procedure

1. Lock acceptance criteria and a maximum pass or cost budget.
2. Score the current artifact against those criteria.
3. Choose the highest-impact repair that can be completed without reopening accepted decisions.
4. Apply the repair and record whether the target metric improved.
5. Stop when criteria pass, no repair has positive expected value, or the budget is reached; otherwise repeat.

## Guardrails

- Mandatory even on strong models: predeclared exit rule; post-repair re-evaluation; mandatory-gate precedence.
- Conflict/precedence: Mandatory acceptance checks outrank a pass budget; if budget expires first, return blocked rather than pass; A newly discovered architecture failure hands off to Surgery or Regenerative Rewrite instead of repeating local passes.
- Stop or fail when: endless recursive polishing; stopping with a known blocking defect.

Full package and provenance: [`bounded-exit`](../../upgradeables/reasoning/bounded-exit/UPGRADEABLE.md).
