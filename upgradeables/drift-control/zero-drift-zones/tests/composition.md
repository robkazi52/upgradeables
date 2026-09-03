# Zero-Drift Zones — Behavioral Expectations

## Positive Activation

- **Given:** Dose, units, contraindication, and exception clause cannot drift while explanation can compress.
- **Expect:** A shorter card with verified critical content.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the user explicitly authorizes change to the marked content
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Latest authorized source correction may replace a zone, with version history retained.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Block release when a required zone fails validation.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** minimal immutable atoms
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A source contains flexible explanation plus one qualified threshold and an exact required warning.
- **Expect:** Freeze the threshold with qualifiers and the warning verbatim, while allowing bounded edits elsewhere.
- **Reject:** Mark everything immutable or paraphrase the warning and round the threshold.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
