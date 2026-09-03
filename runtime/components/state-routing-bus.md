# Task-State Handoff Router (`state-routing-bus@1.1.0`)

Recovered name: State Routing Bus

Purpose: Pass explicit task state, decisions, evidence pointers, and module outputs through real host-supported handoffs.

Activate when: multiple components must exchange typed state.

Do not use when: all work occurs inside one uninterrupted component; the host provides no real file, message, context, or structured-state handoff.

Requires: none.

## Runtime mechanism

Represent the handoff as a typed envelope containing sender, receiver, schema version, authority, provenance, payload, and unresolved status. Validate the envelope and receiver permissions, transmit it through an actual host mechanism such as context, file, message, or database, then require acknowledgement. No latent pointer or hidden channel is assumed.

## Procedure

1. Define the sender, receiver, state schema, and permitted payload fields.
2. Package decisions, evidence pointers, module outputs, provenance, and unresolved items in a bounded envelope.
3. Validate schema, authority, size, and receiver permissions.
4. Transmit through an available explicit host channel and record delivery status.
5. Require acknowledgement or fail with a recoverable handoff record.

## Guardrails

- Mandatory even on strong models: explicit payload, provenance, receiver boundary, and delivery status.
- Conflict/precedence: Host, system, domain, and explicit user authority take precedence over this component; If no real host-supported handoff channel exists, stop or escalate rather than forcing a nominal success.
- Stop or fail when: no real host-supported handoff channel exists; payload schema, authority, provenance, or receiver acknowledgement fails.

Full package and provenance: [`state-routing-bus`](../../upgradeables/orchestration/state-routing-bus/UPGRADEABLE.md).
