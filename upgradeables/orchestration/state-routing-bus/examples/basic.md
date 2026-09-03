# State Routing Bus — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

A research worker hands verified evidence to a separate report writer.

## Why this Upgradeable activates

The writer needs decisions and source pointers but not the worker's full context.

## Inputs / state

Sender/receiver IDs, schema, evidence pointers, decisions, unresolved questions, and message channel.

## What it does

Validates and sends a bounded envelope, then records the writer's acknowledgement.

## What it does not do

Does not claim secret shared memory or transfer private reasoning.

## Result / state change

The writer receives traceable state or the workflow reports a handoff failure.

## Interaction with companion components

StateBlock structures payload; Scoped Loader limits receiver context.
