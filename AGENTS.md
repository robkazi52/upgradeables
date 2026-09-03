# Agent Guide

Start with [START_HERE.md](START_HERE.md).

## When using the library

Complete the user's task. Do not edit this repository merely because you are
using an Upgradeable. Query `runtime/router.json`, prefer an existing task Skill,
then load one `runtime/recipes/` pack. Do not load parallel source, resolved,
runtime, registry, and all-in-one representations of the same recipe.

## When building a Skill

Check `implementations/community/` first. Then read
`MODEL_CONSUMPTION_GUIDE.md`, use
`templates/SKILL_IMPLEMENTATION_TEMPLATE.md`, cite selected `slug@version`
records, and return behavioral/composition tests. A Skill performs a job; it is
not one wrapper per Upgradeable.

## When maintaining this repository

Read the relevant file under `spec/` and `registry/registry.json`. Preserve
archived sources and registry generations. Prefer composition over duplicate
primitives; unresolved concepts stay archival. After any change, run every
validation command listed in `README.md`.
