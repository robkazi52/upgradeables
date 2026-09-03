# CoT-Structured State Block — Behavioral Expectations

## Positive Activation

- **Given:** The handoff needs the basis and open issues, not a transcript of private reasoning.
- **Expect:** Writes those into separate evidence, assumptions, conclusion, uncertainty, and next-action fields. Result: The next analyst can resume and audit the decision basis.
- **Reject:** Omitting the mechanism or instead doing this: It does not publish hidden deliberation or uncited intermediate thoughts.

## Negative Activation

- **Given:** a one-turn answer has no meaningful state
- **Expect:** Remain inactive; do not begin the package-specific first step: Define the minimum state schema and sensitivity boundary.
- **Reject:** Activating CoT-Structured State Block solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Canonical cited evidence overrides stale state summaries.
- **Expect:** Honor the conflict rule and preserve this invariant: separate facts, assumptions, and conclusions
- **Reject:** Silently violating the stated precedence for CoT-Structured State Block

## Failure Boundary

- **Given:** Stop treating the block as authoritative if provenance is missing or fields are stale.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: fact/inference separation
- **Reject:** Claiming a successful CoT-Structured State Block result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** fact/inference separation
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A model has evidence, an assumption, and a tentative conclusion before handoff.
- **Expect:** Expose each in a separately labeled, provenance-aware state record with a next step.
- **Reject:** Return a free-form chain-of-thought transcript or merge the assumption into the facts.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
