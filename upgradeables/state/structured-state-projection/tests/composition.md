# Structured State Projection — Behavioral Expectations

## Positive Activation

- **Given:** It needs claims and source pointers, not identities or strategy notes.
- **Expect:** Citation checking occurs with minimal disclosure and safe merge boundaries.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** one trusted consumer legitimately needs the whole safe state
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Mandatory safety and authority fields override a consumer's request to omit them.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Do not project when required field dependencies or safety constraints are unknown.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** least privilege
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A narrow validator needs three of twenty canonical fields.
- **Expect:** Create a versioned three-field view plus mandatory constraints and validate any response separately.
- **Reject:** Send all twenty fields or let the view become an independent state owner.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
