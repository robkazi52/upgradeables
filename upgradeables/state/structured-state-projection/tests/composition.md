# Structured State Projection — Behavioral Expectations

## Positive Activation

- **Given:** It needs claims and source pointers, not identities or strategy notes.
- **Expect:** Projects claims, citations, relevant constraints, and version metadata with no mutation rights. Result: Citation checking occurs with minimal disclosure and safe merge boundaries.
- **Reject:** Omitting the mechanism or instead doing this: It does not expose identities or allow the checker to edit task authority.

## Negative Activation

- **Given:** one trusted consumer legitimately needs the whole safe state
- **Expect:** Remain inactive; do not begin the package-specific first step: Identify the consumer and its minimum information need.
- **Reject:** Activating Structured State Projection solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Mandatory safety and authority fields override a consumer's request to omit them.
- **Expect:** Honor the conflict rule and preserve this invariant: include mandatory constraints even when they are not task content
- **Reject:** Silently violating the stated precedence for Structured State Projection

## Failure Boundary

- **Given:** Do not project when required field dependencies or safety constraints are unknown.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: least privilege
- **Reject:** Claiming a successful Structured State Projection result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** least privilege
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A narrow validator needs three of twenty canonical fields.
- **Expect:** Create a versioned three-field view plus mandatory constraints and validate any response separately.
- **Reject:** Send all twenty fields or let the view become an independent state owner.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
