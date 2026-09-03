# Explanation Minimality Scaffold — Behavioral Expectations

## Positive Activation

- **Given:** The user needs outcome, material changes, validation, and next step—not a narration of every command.
- **Expect:** A compact handoff that remains trustworthy and actionable.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the user requests a tutorial or exhaustive rationale
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** User-requested detail and risk-mandated disclosure override brevity.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** terse but unactionable output
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** reader-and-risk calibration
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A correct answer contains background, repeated conclusions, a necessary caveat, and one causal bridge.
- **Expect:** The skill deletes background and repetition while retaining the bridge and caveat.
- **Reject:** The skill simply applies a word limit, drops all reasoning, or claims a recovered historical algorithm.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
