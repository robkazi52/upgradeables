# Micro-Repair — Behavioral Expectations

## Positive Activation

- **Given:** The defect is local and the surrounding argument is correct.
- **Expect:** The unsupported claim is removed with no unrelated semantic change.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the artifact architecture is globally wrong
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Do not preserve a frozen neighbor if it is proven part of the defect; explicitly widen the window instead.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** scope creep
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** smallest-fault localization
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** One local unit fails while its neighbors pass.
- **Expect:** The skill freezes passing neighbors, changes the minimum atoms, checks boundaries, and escalates if the defect proves systemic.
- **Reject:** The skill rewrites the section for general improvement or applies repeated local patches to broken architecture.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
