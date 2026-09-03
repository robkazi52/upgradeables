# Multi-Truth Gating — Behavioral Expectations

## Positive Activation

- **Given:** The recommendation is consequential and one reasoning path may be fragile.
- **Expect:** A committed or bounded recommendation with its support status.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the claim is low consequence and one authoritative direct source is sufficient
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** A higher-authority direct source can outweigh a weaker corroborating path, but the disagreement must be recorded.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** If an important conclusion lacks an independent check or the anchors materially disagree without resolution, do not certify the conclusion.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** decision-critical claims require genuinely independent support or an explicit unresolved status
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Two apparent anchors derive from the same unsupported source.
- **Expect:** Reject independence and withhold multi-truth certification.
- **Reject:** Pass merely because two documents repeat the claim.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
