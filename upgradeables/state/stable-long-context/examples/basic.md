# Basic composition example

**Situation:** large corpus or long-running workflow.

**Composition:** establish a task lock, activate `stable-long-context`, preserve
explicit state and evidence boundaries, then pass the result through the
workflow's applicable validator.

**Expected:** the component performs only its documented purpose and reports
uncertainty or failure instead of manufacturing missing support.
