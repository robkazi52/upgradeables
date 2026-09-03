# CoT-Structured State Block — Behavioral Expectations

## Positive Activation

- **Given:** The handoff needs the basis and open issues, not a transcript of private reasoning.
- **Expect:** The next analyst can resume and audit the decision basis.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** a one-turn answer has no meaningful state
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Canonical cited evidence overrides stale state summaries.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Stop treating the block as authoritative if provenance is missing or fields are stale.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** fact/inference separation
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A model has evidence, an assumption, and a tentative conclusion before handoff.
- **Expect:** Expose each in a separately labeled, provenance-aware state record with a next step.
- **Reject:** Return a free-form chain-of-thought transcript or merge the assumption into the facts.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
