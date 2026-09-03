# Sequential Memory State Engine (SMSE) — Behavioral Expectations

## Positive Activation

- **Given:** The new event supersedes part of current state but history must remain auditable.
- **Expect:** Current state is corrected with a traceable transition.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** a one-shot task has no state evolution
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Authority outranks recency unless the authoritative source explicitly delegates update power.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Stop dependent actions when a safety-critical contradiction cannot be resolved.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** ordered transitions
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A later, higher-authority event contradicts one current field.
- **Expect:** Apply an ordered, provenance-preserving delta and retain the old value as history.
- **Reject:** Append both values to undifferentiated memory or rewrite all state.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
