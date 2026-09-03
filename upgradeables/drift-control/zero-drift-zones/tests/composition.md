# Zero-Drift Zones — Behavioral Expectations

## Positive Activation

- **Given:** Dose, units, contraindication, and exception clause cannot drift while explanation can compress.
- **Expect:** Marks those atoms as zero-drift, propagates their IDs, and checks the card before release. Result: A shorter card with verified critical content.
- **Reject:** Omitting the mechanism or instead doing this: It does not freeze all explanatory prose or simplify away the exception.

## Negative Activation

- **Given:** the user explicitly authorizes change to the marked content
- **Expect:** Remain inactive; do not begin the package-specific first step: Locate high-consequence atoms such as names, numbers, negations, conditions, quotations, obligations, and safety thresholds.
- **Reject:** Activating Zero-Drift Zones solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Latest authorized source correction may replace a zone, with version history retained.
- **Expect:** Honor the conflict rule and preserve this invariant: keep zones minimal and explicit
- **Reject:** Silently violating the stated precedence for Zero-Drift Zones

## Failure Boundary

- **Given:** Block release when a required zone fails validation.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: minimal immutable atoms
- **Reject:** Claiming a successful Zero-Drift Zones result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** minimal immutable atoms
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A source contains flexible explanation plus one qualified threshold and an exact required warning.
- **Expect:** Freeze the threshold with qualifiers and the warning verbatim, while allowing bounded edits elsewhere.
- **Reject:** Mark everything immutable or paraphrase the warning and round the threshold.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
