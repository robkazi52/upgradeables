# Meta-Stability Mode — Behavioral Expectations

## Positive Activation

- **Given:** Repeated changes and divergent state threaten global coherence.
- **Expect:** One coherent baseline and a controlled resume queue.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** one local defect can be repaired directly
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** A user-approved newer decision is not rolled back solely because an older checkpoint is internally coherent.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** stability theater
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** verified checkpoint
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Repeated changes and module conflicts cause state versions to diverge.
- **Expect:** The skill freezes optional change, restores or rebuilds a verified checkpoint, quarantines deltas, checks coherence, and resumes gradually.
- **Reject:** The skill only retries the failed action, enters SAFE, or permanently halts work.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
