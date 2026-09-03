# Basic composition example

**Situation:** an action is costly, irreversible, or dependency-sensitive.

**Composition:** establish a task lock, activate `forethought-checkpoints`, preserve
explicit state and evidence boundaries, then pass the result through the
workflow's applicable validator.

**Expected:** the component performs only its documented purpose and reports
uncertainty or failure instead of manufacturing missing support.
