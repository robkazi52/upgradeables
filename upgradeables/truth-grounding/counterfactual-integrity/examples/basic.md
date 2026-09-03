# Counterfactual Integrity Gate — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

A policy analyst asks what might happen if a threshold were doubled while also requesting a summary of current policy.

## Why this Upgradeable activates

The answer combines factual and counterfactual modes.

## Inputs / state

Current threshold from the source plus an explicitly hypothetical doubled threshold.

## What it does

Keeps the current rule factual and reports projected effects under a labeled hypothetical branch.

## What it does not do

State that the threshold was actually changed.

## Result / state change

Two separated sections with no phase leakage.

## Interaction with companion components

['domain-mode-isolation', 'epistemic-status-gating', 'grounding-no-invention']
