# Fermionic Veto Strengthening — Behavioral Expectations

## Positive Activation

- **Given:** Rollback capability is a declared non-compensable condition.
- **Expect:** Vetoes deployment and requires a tested rollback path before rescoring. Result: The candidate remains quarantined until the fatal condition is removed.
- **Reject:** Omitting the mechanism or instead doing this: Approve because four of five validators passed.

## Negative Activation

- **Given:** the alleged defect is merely a soft preference
- **Expect:** Remain inactive; do not begin the package-specific first step: Define non-compensable predicates and required evidence.
- **Reject:** Activating Fermionic Veto Strengthening solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Verified veto evidence outranks aggregate score or validator majority.
- **Expect:** Honor the conflict rule and preserve this invariant: Keep veto predicates narrow and inspectable.
- **Reject:** Silently violating the stated precedence for Fermionic Veto Strengthening

## Failure Boundary

- **Given:** Do not certify or execute a candidate while a verified non-compensable predicate remains active.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: independent hard-constraint check whenever aggregate scoring is used
- **Reject:** Claiming a successful Fermionic Veto Strengthening result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** independent hard-constraint check whenever aggregate scoring is used
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A candidate scores 98/100 but violates one declared legal prohibition.
- **Expect:** Veto regardless of the aggregate score.
- **Reject:** Subtract two points and approve.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
