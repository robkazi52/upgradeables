# Clarification Gateway — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

A user asks for a shipping quote but gives a city shared by two states.

## Why this Upgradeable activates

Destination changes price and feasibility.

## Inputs / state

City supplied; state and postal code absent; questions permitted.

## What it does

Asks one focused destination question before pricing and records the answer.

## What it does not do

It does not guess the state or ask unrelated preference questions.

## Result / state change

A resolved destination field or an explicit inability to quote.

## Interaction with companion components

['task-set-lock-in']
