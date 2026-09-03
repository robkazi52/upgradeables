# Independent Evidence Gate (`multi-truth-gating@1.1.0`)

Recovered name: Multi-Truth Gating

Purpose: Reduce dependence on one fragile source, inference chain, or evaluator before a consequential conclusion is committed.

Activate when: an important conclusion rests on fragile evidence.

Do not use when: the claim is low consequence and one authoritative direct source is sufficient; the supposed anchors merely duplicate the same underlying source.

Requires: none.

## Runtime mechanism

For each decision-critical conclusion, identify a primary factual anchor and at least one genuinely independent corroborating anchor or verification path. Compare what each supports; convergence permits commitment, while material divergence triggers re-evaluation, a narrower claim, explicit uncertainty, or abstention.

## Procedure

1. Identify conclusions whose failure would materially change the outcome.
2. Record the primary evidence or reasoning anchor for each.
3. Select an independent corroborating source or validation path.
4. Check independence and compare the supported propositions.
5. Resolve differences by evidence and authority rules rather than averaging.

## Guardrails

- Mandatory even on strong models: decision-critical claims require genuinely independent support or an explicit unresolved status.
- Conflict/precedence: A higher-authority direct source can outweigh a weaker corroborating path, but the disagreement must be recorded; Safety vetoes are not overridable by numerical agreement among other checks.
- Stop or fail when: If an important conclusion lacks an independent check or the anchors materially disagree without resolution, do not certify the conclusion.

Full package and provenance: [`multi-truth-gating`](../../upgradeables/truth-grounding/multi-truth-gating/UPGRADEABLE.md).
