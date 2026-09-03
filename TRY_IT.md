# Try These Five Things

You do not need to learn the architecture first. Copy one prompt into a new chat
with a model that can open links. Replace the bracketed text and let it do the work.
If the model cannot open links, attach
[`dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md`](dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md).

## 1. Improve a difficult prompt

```text
Read https://raw.githubusercontent.com/robkazi52/upgradeables/main/START_HERE.md. Improve the prompt below for reliable use, selecting only Upgradeables that address a concrete failure risk. Return the improved copy-ready prompt, a short keep/drop explanation, and three tests. Do not merely explain the framework.

[PASTE YOUR PROMPT]
```

## 2. Review a pull request

```text
Read https://raw.githubusercontent.com/robkazi52/upgradeables/main/START_HERE.md. Review the pull request below for bugs, regressions, unsafe assumptions, and missing tests. Start from the code-review recipe, keep only triggered components, cite file and line evidence, and do not edit unless I ask.

[PASTE THE DIFF OR PR LINK]
```

## 3. Research five sources

```text
Read https://raw.githubusercontent.com/robkazi52/upgradeables/main/START_HERE.md. Answer my question using only the five supplied sources. Keep facts separate from inference, attach citations to material claims, expose conflicts, and abstain where the sources do not support an answer.

Question: [QUESTION]
Sources: [FIVE LINKS OR ATTACHED FILES]
```

## 4. Analyze a long document

```text
Read https://raw.githubusercontent.com/robkazi52/upgradeables/main/START_HERE.md. Analyze the attached long document for the objective below. Use bounded loading and explicit state, preserve quotations and identifiers exactly, and return findings, evidence locations, unresolved gaps, and a continuation snapshot if the work exceeds one context.

Objective: [WHAT YOU NEED]
```

## 5. Turn your workflow into a Skill

```text
Read https://raw.githubusercontent.com/robkazi52/upgradeables/main/START_HERE.md and https://raw.githubusercontent.com/robkazi52/upgradeables/main/MODEL_CONSUMPTION_GUIDE.md. Turn the workflow below into a portable task-oriented SKILL.md. Select the smallest useful Upgradeable composition, cite slug@version, state host assumptions and exclusions, and include positive, negative, failure, composition, and authority-conflict tests.

Workflow: [DESCRIBE YOUR REPEATED WORK]
```

These are starting points. Host and user instructions still win, and the
repository cannot grant browsing, tools, persistence, or write permission.
