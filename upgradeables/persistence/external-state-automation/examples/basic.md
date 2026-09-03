# External State Automation — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

A multi-day literature review must resume after context resets.

## Why this Upgradeable activates

Verified decisions and source pointers need durable continuation.

## Inputs / state

State snapshot, project file permission, schema version, provenance, and retention policy.

## What it does

Writes the compact snapshot to an authorized file, verifies it, and validates it on resume.

## What it does not do

Does not claim persistence before the write succeeds or store the whole conversation by default.

## Result / state change

The next session restores traceable state or receives an explicit failure/staleness warning.

## Interaction with companion components

State Snapshot creates the payload; State Routing Bus delivers it after restore.
