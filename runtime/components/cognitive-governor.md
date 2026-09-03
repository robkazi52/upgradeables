# Reasoning Effort Budget Controller (`cognitive-governor@1.1.0`)

Recovered name: Reasoning Budget / Cognitive Governor

Purpose: Prevent both expensive overthinking of trivial work and unsafe underchecking of consequential work.

Activate when: effort allocation materially affects cost or quality.

Do not use when: a mandatory protocol fixes the review budget; the task is a trivial deterministic transformation.

Requires: none.

## Runtime mechanism

Estimate a total effort envelope from complexity, uncertainty, consequence, irreversibility, and the expected value of another check. Allocate caps for planning, execution, and validation, reserve extra capacity for high-risk unknowns, and periodically compare remaining defect or uncertainty value with remaining cost. The governor owns how much total reasoning is justified; it does not choose which regions receive that effort or how much work flows concurrently.

## Procedure

1. Classify task complexity, uncertainty, consequence, and reversibility.
2. Set an effort envelope and mandatory validation floor.
3. Divide the envelope among planning, execution, verification, and contingency.
4. Track evidence gained, defects removed, and budget consumed at milestones.
5. Increase the envelope only when newly exposed risk has positive expected value; otherwise invoke the exit rule.

## Guardrails

- Mandatory even on strong models: risk-based validation floor; marginal-value review; explicit stop or escalation.
- Conflict/precedence: Risk-mandated validation overrides a lower convenience budget; If the envelope cannot cover hard checks, return an explicit resource or evidence blocker.
- Stop or fail when: over-polishing; premature exit.

Full package and provenance: [`cognitive-governor`](../../upgradeables/meta-control/cognitive-governor/UPGRADEABLE.md).
