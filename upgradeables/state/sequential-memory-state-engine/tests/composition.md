# Sequential Memory State Engine (SMSE) — Behavioral Expectations

## Positive Activation

- **Given:** The new event supersedes part of current state but history must remain auditable.
- **Expect:** Normalizes the correction, resolves the conflict, commits version 13, and refreshes the support-agent view. Result: Current state is corrected with a traceable transition.
- **Reject:** Omitting the mechanism or instead doing this: It does not delete the earlier classification or keep both values current.

## Negative Activation

- **Given:** a one-shot task has no state evolution
- **Expect:** Remain inactive; do not begin the package-specific first step: Ingest one event with source, time, and authority metadata.
- **Reject:** Activating Sequential Memory State Engine (SMSE) solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Authority outranks recency unless the authoritative source explicitly delegates update power.
- **Expect:** Honor the conflict rule and preserve this invariant: preserve event order and provenance
- **Reject:** Silently violating the stated precedence for Sequential Memory State Engine (SMSE)

## Failure Boundary

- **Given:** Stop dependent actions when a safety-critical contradiction cannot be resolved.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: ordered transitions
- **Reject:** Claiming a successful Sequential Memory State Engine (SMSE) result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** ordered transitions
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A later, higher-authority event contradicts one current field.
- **Expect:** Apply an ordered, provenance-preserving delta and retain the old value as history.
- **Reject:** Append both values to undifferentiated memory or rewrite all state.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
