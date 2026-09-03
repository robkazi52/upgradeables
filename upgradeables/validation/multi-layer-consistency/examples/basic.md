# Multi-Layer Consistency — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

Every module test passes, but the application claims all writes are transactional.

## Why this Upgradeable activates

The global guarantee depends on cross-module composition.

## Inputs / state

Module behaviors, integration flow, and transactional invariant.

## What it does

Traces the invariant down and finds one inter-module path committing before validation.

## What it does not do

Approve because each module is locally correct.

## Result / state change

A cross-layer mismatch blocks the global guarantee until integration behavior changes.

## Interaction with companion components

['parallel-qms', 'bidirectional-consistency', 'coherence-loops']
