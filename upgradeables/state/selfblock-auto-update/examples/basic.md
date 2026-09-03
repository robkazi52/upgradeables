# SelfBlock Auto-Update — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

An agent finishes validating dataset column types.

## Why this Upgradeable activates

The completion and two discovered anomalies change live task state.

## Inputs / state

State version 8, validation output, immutable objective, and mutable progress/anomaly fields.

## What it does

Writes a version-checked delta marking validation complete and adding cited anomalies.

## What it does not do

It does not rewrite the objective or infer that the entire project is complete.

## Result / state change

Version 9 accurately reflects progress and exceptions.

## Interaction with companion components

['stateblock', 'sequential-memory-state-engine', 'working-memory-lock-in']
