# State Snapshot — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

A research agent hands an unfinished review to another session.

## Why this Upgradeable activates

The second session must know exactly which sources and claims were accepted at handoff.

## Inputs / state

State version 21, schema v3, evidence index, open questions, and next action.

## What it does

Freezes those fields with integrity and predecessor metadata, then verifies new events on restore.

## What it does not do

It does not treat the copy as live or omit unresolved questions.

## Result / state change

The review resumes from a reproducible checkpoint.

## Interaction with companion components

['stateblock', 'stable-long-context', 'sequential-memory-state-engine']
