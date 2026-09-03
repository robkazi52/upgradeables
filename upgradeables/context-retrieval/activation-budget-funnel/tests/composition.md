# Activation-Budget Funnel — Behavioral Expectations

## Positive Activation

- **Given:** All proposals cannot remain active without recency and attention competition.
- **Expect:** Processes bounded batches, captures criterion evidence, indexes it, releases raw text, then compares from the index and verifies finalists. Result: A complete comparison built from traceable evidence cards with a bounded live workspace.
- **Reject:** Omitting the mechanism or instead doing this: It does not draft the recommendation while still pulling unindexed proposal text.

## Negative Activation

- **Given:** a short single source fits comfortably in context
- **Expect:** Remain inactive; do not begin the package-specific first step: Define the question and the evidence fields the task needs.
- **Reject:** Activating Activation-Budget Funnel solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Source-boundary and authority rules control what may enter the funnel.
- **Expect:** Honor the conflict rule and preserve this invariant: Separate retrieval/capture from synthesis.
- **Reject:** Silently violating the stated precedence for Activation-Budget Funnel

## Failure Boundary

- **Given:** Pause synthesis when evidence has not been captured with provenance or active pulls cannot be bounded without losing required coverage.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: retrieval-before-synthesis separation
- **Reject:** Claiming a successful Activation-Budget Funnel result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** retrieval-before-synthesis separation
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Ten sources and a request for an evidence-grounded decision.
- **Expect:** Capture and index evidence in bounded batches before synthesis, then verify the decision against source pointers.
- **Reject:** Load all sources and interleave retrieval with unsupported decision writing.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
