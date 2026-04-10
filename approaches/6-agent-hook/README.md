# Approach 6: Agent Hook

## Configuration

A Stop hook in `.claude/settings.local.json` using an `agent` hook type. Instead of running a shell command, this spawns a sub-agent that runs pyrefly and interprets the results.

```json
{
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "agent",
        "prompt": "Verify that all Python files in the src/ directory pass pyrefly type checking. Run `pyrefly check src/` and check the results. If there are any type errors, return ok: false with the errors. $ARGUMENTS",
        "timeout": 120
      }]
    }]
  }
}
```

## How It Works

1. When Claude stops, the hook spawns a sub-agent with the given prompt
2. The sub-agent runs `pyrefly check src/` and evaluates the output
3. If there are type errors, the agent returns `ok: false` with the errors — Claude continues working to fix them
4. If pyrefly passes, the agent returns `ok: true` and Claude stops normally
