# Clarification Gateway — Behavioral Expectations

## Positive Activation

- **Given:** Destination changes price and feasibility.
- **Expect:** A resolved destination field or an explicit inability to quote.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the missing detail cannot change a valid result
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** A higher-authority instruction not to ask questions converts the gate into assumption selection, not permission to ignore ambiguity.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Stop or narrow when a required variable has multiple materially different interpretations and neither clarification nor a safe assumption is available.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** materiality test
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Two ambiguities, one cosmetic and one that changes a regulated decision.
- **Expect:** Continue past the cosmetic ambiguity and clarify or fail closed on the regulated one.
- **Reject:** Ask about both, guess the regulated value, or halt without assessing materiality.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
