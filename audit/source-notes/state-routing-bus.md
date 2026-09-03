# Source Note — State Routing Bus

- Slug: `state-routing-bus`
- ID: `A-02`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — A-02. Teleport Bus (current_consolidated_catalog)

## Recovered or normalized purpose

Pass explicit task state, decisions, evidence pointers, and module outputs through real host-supported handoffs.

## Operational mechanism

Represent the handoff as a typed envelope containing sender, receiver, schema version, authority, provenance, payload, and unresolved status. Validate the envelope and receiver permissions, transmit it through an actual host mechanism such as context, file, message, or database, then require acknowledgement. No latent pointer or hidden channel is assumed.

## Trigger and task use

Triggers: Activate when the task requires multiple components exchange state.. Best-fit tasks: multi-agent workflows, modular Skills, cross-process continuation.

## Interactions and failure boundary

Companions: stateblock, state-snapshot. Failure boundary: no real host-supported handoff channel exists; payload schema, authority, provenance, or receiver acknowledgement fails.

## Unresolved details / interpretation boundary

Historical identity, purpose, and core behavior are recovered; v0.2 states the mechanism explicitly without claiming hidden capabilities.
