# Placeholder Suppression — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

Publish a generated GitHub repository.

## Why this Upgradeable activates

README templates, manifests, and examples may retain setup prompts or dummy URLs.

## Inputs / state

Repository files, manifest schema, approved example fixtures, and project metadata are available.

## What it does

Finds a `[your-org]` README token, an empty license field, and `example.com` in a test fixture; resolves the first two and allowlists the fixture by path before rescanning.

## What it does not do

Replace the license with a guess or globally allow every `example.com` occurrence.

## Result / state change

A release with no accidental placeholders and one documented intentional fixture.

## Interaction with companion components

['safe-rewrite', 'grounding-no-invention']
