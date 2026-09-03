# Work with Long Documents Prompt

```text
Process the attached long document or corpus while preserving source fidelity.

If you can browse GitHub, read:
https://raw.githubusercontent.com/robkazi52/upgradeables/main/START_HERE.md
Then use the long-context-source-fidelity recipe with only triggered components.

Requirements:
- Lock the task and source boundary before processing.
- Work in bounded chunks and maintain an explicit compact ledger of facts, decisions, unresolved items, and source locations.
- Keep source text separate from inference and working notes.
- Periodically check for omissions, contradictions, and task drift.
- Do not claim to remember material outside the available context. Ask for the next chunk or a state snapshot when necessary.
- Verify the final result against the source and fail closed on text that cannot be confirmed.

Task: [SUMMARIZE / EXTRACT / COMPARE / TRANSFORM / OTHER]
Document or corpus: [ATTACH OR PASTE]
Required fidelity and citation format: [REQUIREMENTS]
Final output: [FORMAT]
```
