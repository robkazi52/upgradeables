# Structured Refinement Cycles — Behavioral Expectations

## Positive Activation

- **Given:** The draft has two incorrect dates, a duplicated section, and inconsistent voice.
- **Expect:** A release-ready guide with traceable pass boundaries and no semantic regression.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** only one bounded defect exists
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Factual correctness outranks structural elegance and style.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** mixed-objective drift
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** dependency order
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** An artifact has factual, structural, and stylistic defects.
- **Expect:** The skill classifies them, fixes them in dependency order, locks prior-pass decisions, and validates across classes.
- **Reject:** The skill performs one blended rewrite or iterates without pass boundaries.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
