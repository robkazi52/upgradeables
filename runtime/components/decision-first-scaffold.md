# Decision-First Scaffold (`decision-first-scaffold@1.1.0`)

Purpose: Keep analysis shaped around a decision, options, and decision criteria rather than accumulating directionless detail.

Activate when: analysis risks becoming directionless before commitment.

Do not use when: the task asks only for faithful extraction or description; the decision owner or available options are unknown.

Requires: none.

## Runtime mechanism

Modern conservative interpretation: write a decision sentence with owner, options, criteria, and deadline or commitment point; then admit analysis only when it changes an option score, exposes a constraint, or reduces a named uncertainty. The historical corpus recovers the exact name but not this mechanism.

## Procedure

1. State the decision in one sentence, including who will act.
2. List viable options, including defer or gather-more-evidence where legitimate.
3. Lock decision criteria and non-negotiable constraints.
4. Map each analysis question to a criterion or uncertainty.
5. Produce a recommendation with the evidence and unresolved uncertainty that drives it.

## Guardrails

- Mandatory even on strong models: explicit decision statement; criterion linkage; uncertainty-aware outcome.
- Conflict/precedence: If the user requests exploration without commitment, do not impose a final choice; If evidence cannot support any option, return the missing evidence rather than a fabricated recommendation.
- Stop or fail when: invented historical mechanics; premature option closure.

Full package and provenance: [`decision-first-scaffold`](../../upgradeables/reasoning/decision-first-scaffold/UPGRADEABLE.md).
