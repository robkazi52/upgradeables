# Clarification Gateway — Behavioral Expectations

## Positive Activation

- **Given:** Destination changes price and feasibility.
- **Expect:** Asks one focused destination question before pricing and records the answer. Result: A resolved destination field or an explicit inability to quote.
- **Reject:** Omitting the mechanism or instead doing this: It does not guess the state or ask unrelated preference questions.

## Negative Activation

- **Given:** the missing detail cannot change a valid result
- **Expect:** Remain inactive; do not begin the package-specific first step: Extract missing variables, ambiguous terms, and instruction conflicts before substantive execution.
- **Reject:** Activating Clarification Gateway solely because its name appears relevant

## Precedence Or Conflict

- **Given:** A higher-authority instruction not to ask questions converts the gate into assumption selection, not permission to ignore ambiguity.
- **Expect:** Honor the conflict rule and preserve this invariant: Explain why a requested clarification changes the result.
- **Reject:** Silently violating the stated precedence for Clarification Gateway

## Failure Boundary

- **Given:** Stop or narrow when a required variable has multiple materially different interpretations and neither clarification nor a safe assumption is available.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: materiality test
- **Reject:** Claiming a successful Clarification Gateway result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** materiality test
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Two ambiguities, one cosmetic and one that changes a regulated decision.
- **Expect:** Continue past the cosmetic ambiguity and clarify or fail closed on the regulated one.
- **Reject:** Ask about both, guess the regulated value, or halt without assessing materiality.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
