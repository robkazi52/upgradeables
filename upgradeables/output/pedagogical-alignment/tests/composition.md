# Pedagogical Alignment Constraint — Behavioral Expectations

## Positive Activation

- **Given:** They need impact and rollout logic, not implementation-level type-system detail.
- **Expect:** A technically faithful explanation that supports planning decisions.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the audience and purpose cannot be inferred and the choice materially changes content
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Accuracy, scope, and uncertainty outrank ease of explanation.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** oversimplification
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** internal prerequisite model
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** An accurate explanation assumes several prerequisites the target reader lacks.
- **Expect:** The skill models the gap, orders prerequisites, defines terms, and back-checks simplifications.
- **Reject:** The skill merely makes sentences shorter, changes tone, or removes technical limitations.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
