# Drift Suppression — Behavioral Expectations

## Positive Activation

- **Given:** The qualification is a narrow-corridor claim and the output crossed it.
- **Expect:** The repaired summary preserves the source condition.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** no semantic baseline or allowed corridor exists
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Latest authorized task/source state defines the baseline, not the oldest lock by default.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Stop publication when a high-impact deviation cannot be repaired or adjudicated.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** source/task baseline
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A transformed artifact differs from source both stylistically and in one qualified claim.
- **Expect:** Accept permitted style variation, classify the claim change as drift, and repair only that region.
- **Reject:** Reject all difference or ignore the semantic change.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
