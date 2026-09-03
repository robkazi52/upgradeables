# Pedagogical Alignment Constraint — Behavioral Expectations

## Positive Activation

- **Given:** They need impact and rollout logic, not implementation-level type-system detail.
- **Expect:** Starts with user-visible impact, defines compatibility window in plain language, sequences rollout dependencies, and includes one workflow example while preserving rollback limits. Result: A technically faithful explanation that supports planning decisions.
- **Reject:** Omitting the mechanism or instead doing this: Replace the mechanism with a false everyday analogy or omit the irreversible deadline.

## Negative Activation

- **Given:** the audience and purpose cannot be inferred and the choice materially changes content
- **Expect:** Remain inactive; do not begin the package-specific first step: Identify the reader's likely starting knowledge and the capability they need after reading.
- **Reject:** Activating Pedagogical Alignment Constraint solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Accuracy, scope, and uncertainty outrank ease of explanation.
- **Expect:** Honor the conflict rule and preserve this invariant: preserve accuracy before accessibility
- **Reject:** Silently violating the stated precedence for Pedagogical Alignment Constraint

## Failure Boundary

- **Given:** oversimplification
- **Expect:** Stop, narrow, abstain, or escalate while preserving: internal prerequisite model
- **Reject:** Claiming a successful Pedagogical Alignment Constraint result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** internal prerequisite model
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** An accurate explanation assumes several prerequisites the target reader lacks.
- **Expect:** The skill models the gap, orders prerequisites, defines terms, and back-checks simplifications.
- **Reject:** The skill merely makes sentences shorter, changes tone, or removes technical limitations.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
