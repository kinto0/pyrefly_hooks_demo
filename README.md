# Pyrefly + Claude Code: Hook vs Skill vs CLAUDE.md

## The Question

How do you enforce type checking with Pyrefly in Claude Code? We tested 5 approaches.

## Results Summary

| Approach | Ran pyrefly? | Fixed errors? | Enforcement |
|---|---|---|---|
| Skill (gentle) | No | No | None — Claude skipped it |
| Skill (mandatory) | No | No | None — still skipped |
| CLAUDE.md | Yes | Yes | Voluntary (~80-90%) |
| Hook (Stop + exit 2) | Yes | Yes | Enforced (100%) |
| Hook (retry limit) | Yes | Yes | Enforced (3 attempts, then warns) |

## Testing Each Approach

Each test starts with type errors in `src/converter.py`. Reset them before each test:

```python
# In main(), use these intentionally wrong calls:
temp = to_celsius("hot")          # str instead of float
weight = to_kg([150])             # list instead of float
result = format_result("100", 42) # str and int instead of float and str
```

### Test 1: Gentle Skill

Setup: Copy `approaches/1-skill-gentle/` config into `.claude/`. Remove hooks and CLAUDE.md.

Prompt:
> Add a to_liters(gallons: float) -> float function to src/converter.py that converts gallons to liters. Add a demo call in main().

Result: Claude adds the function but does not run pyrefly. Type errors remain.

### Test 2: Mandatory Skill

Setup: Copy `approaches/2-skill-mandatory/` config into `.claude/`. Remove hooks and CLAUDE.md.

Prompt:
> Add a to_meters(feet: float) -> float function to src/converter.py that converts feet to meters. Add a demo call in main().

Result: Claude does not run pyrefly. Type errors remain.

### Test 3: CLAUDE.md

Setup: Copy `approaches/3-claude-md/CLAUDE.md` to project root. Remove hooks and skills.

Prompt:
> Add a to_inches(cm: float) -> float function to src/converter.py that converts cm to inches. Add a demo call in main().

Result: Claude adds the function, runs pyrefly, fixes errors, confirms 0 errors.

### Test 4: Stop Hook (exit 2)

Setup: Copy `approaches/4-hook-stop-exit2/settings.local.json` to `.claude/`. Remove CLAUDE.md and skills.

Prompt:
> Add a to_fahrenheit(celsius: float) -> float function to src/converter.py. Add a demo call in main().

Result: Claude adds the function, Stop hook fires, pyrefly catches errors, Claude auto-fixes, hook passes.

### Test 5: Hook with Retry Limit

Setup: Copy `approaches/5-hook-with-retry-limit/` configs. Remove CLAUDE.md and skills.

Prompt:
> Add a to_stones(kg: float) -> float function to src/converter.py. Add a demo call in main().

Result: Same as Test 4, but gives up after 3 failed attempts.

## Reproducing

1. Clone this directory
2. Copy the approach you want into `.claude/settings.local.json` or `CLAUDE.md`
3. Introduce type errors in `src/converter.py` main()
4. Ask Claude to add a feature and observe the behavior

## Approach Details

See the `approaches/` directory for each configuration:

- `1-skill-gentle/` — Soft skill description, Claude ignored it
- `2-skill-mandatory/` — Forceful skill description, Claude still ignored it
- `3-claude-md/` — CLAUDE.md with mandatory rules, Claude followed them
- `4-hook-stop-exit2/` — Stop hook, enforced at infrastructure level
- `5-hook-with-retry-limit/` — Stop hook with 3-attempt limit, best for production
