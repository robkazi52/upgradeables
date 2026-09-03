# Multi-Truth Gating — Behavioral Expectations

## Positive Activation

- **Given:** The recommendation is consequential and one reasoning path may be fragile.
- **Expect:** Compares independent support and narrows the recommendation if causal support diverges. Result: A committed or bounded recommendation with its support status.
- **Reject:** Omitting the mechanism or instead doing this: Treat repeated citations to the same study as multiple truths.

## Negative Activation

- **Given:** the claim is low consequence and one authoritative direct source is sufficient
- **Expect:** Remain inactive; do not begin the package-specific first step: Identify conclusions whose failure would materially change the outcome.
- **Reject:** Activating Multi-Truth Gating solely because its name appears relevant

## Precedence Or Conflict

- **Given:** A higher-authority direct source can outweigh a weaker corroborating path, but the disagreement must be recorded.
- **Expect:** Honor the conflict rule and preserve this invariant: Test anchor independence.
- **Reject:** Silently violating the stated precedence for Multi-Truth Gating

## Failure Boundary

- **Given:** If an important conclusion lacks an independent check or the anchors materially disagree without resolution, do not certify the conclusion.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: decision-critical claims require genuinely independent support or an explicit unresolved status
- **Reject:** Claiming a successful Multi-Truth Gating result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** decision-critical claims require genuinely independent support or an explicit unresolved status
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Two apparent anchors derive from the same unsupported source.
- **Expect:** Reject independence and withhold multi-truth certification.
- **Reject:** Pass merely because two documents repeat the claim.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
