# Approach 5: Stop Hook with Retry Limit

## Configuration

Approach 4 with a safety valve — gives Claude 3 attempts to fix errors per session, then lets it stop.

```json
{
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "command",
        "command": "bash 5-hook-with-retry-limit/pyrefly-hook.sh",
        "timeout": 30
      }]
    }]
  }
}
```

## The Script

`pyrefly-hook.sh` reads `session_id` from Claude Code's stdin JSON for per-session counting:

1. Reads JSON from stdin (Claude Code passes hook context with `session_id`, `tool_name`, etc.)
2. Extracts `session_id` using grep/sed (no jq dependency)
3. Counter file is per-session: `/tmp/.pyrefly-hook-count-{session_id}`
4. Each `pyrefly check` failure increments the counter and exits 2 (blocking)
5. After 3 failures, exits 0 with a WARNING (non-blocking) — counter stays at max for the rest of the session
6. When pyrefly passes (errors fixed), the counter file is cleaned up
7. New agent session = new session_id = fresh counter
