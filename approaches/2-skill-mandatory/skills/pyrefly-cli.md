---
name: pyrefly-cli
description: MANDATORY type checker. You MUST run this before completing ANY task that modifies Python files. Never skip this step.
---

IMPORTANT: Before completing any task that creates or modifies Python files, you MUST:
1. Run `pyrefly check` at the root of the project
2. If there are any type errors, fix ALL of them
3. Run `pyrefly check` again to confirm 0 errors
4. Only THEN report the task as complete

This is NOT optional. Never skip type checking. Never report completion without 0 pyrefly errors.
