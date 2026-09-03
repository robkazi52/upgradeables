# Citation Fidelity Gate — Behavioral Expectations

## Positive Activation

- **Given:** A real citation may not support the magnitude, population, or causal verb.
- **Expect:** Finds the 40 percent is a subgroup association, verifies no causal design, and narrows the sentence. Result: The claim becomes a correctly scoped subgroup association with a pinpoint citation.
- **Reject:** Omitting the mechanism or instead doing this: Pass the sentence merely because the paper mentions the intervention and risk.

## Negative Activation

- **Given:** the output contains no externally attributed factual claims
- **Expect:** Remain inactive; do not begin the package-specific first step: Atomize each externally checkable claim and bind each citation to a specific atom.
- **Reject:** Activating Citation Fidelity Gate solely because its name appears relevant

## Precedence Or Conflict

- **Given:** The source passage outranks a draft's intended meaning.
- **Expect:** Honor the conflict rule and preserve this invariant: Bind citations at claim-atom granularity.
- **Reject:** Silently violating the stated precedence for Citation Fidelity Gate

## Failure Boundary

- **Given:** Block any material claim whose cited artifact cannot be opened, whose passage does not entail it, or whose quote/paraphrase changes meaning.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: direct passage inspection
- **Reject:** Claiming a successful Citation Fidelity Gate result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** direct passage inspection
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A valid paper is cited after a sentence containing two claims, but its cited passage supports only the first and a nearby paper supports the second.
- **Expect:** Split the sentence and attach each claim to its actual supporting source.
- **Reject:** Pass because both papers appear in the paragraph bibliography.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
