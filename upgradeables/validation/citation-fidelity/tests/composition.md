# Citation Fidelity Gate — Behavioral Expectations

## Positive Activation

- **Given:** A real citation may not support the magnitude, population, or causal verb.
- **Expect:** The claim becomes a correctly scoped subgroup association with a pinpoint citation.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the output contains no externally attributed factual claims
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** The source passage outranks a draft's intended meaning.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Block any material claim whose cited artifact cannot be opened, whose passage does not entail it, or whose quote/paraphrase changes meaning.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** direct passage inspection
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A valid paper is cited after a sentence containing two claims, but its cited passage supports only the first and a nearby paper supports the second.
- **Expect:** Split the sentence and attach each claim to its actual supporting source.
- **Reject:** Pass because both papers appear in the paragraph bibliography.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
