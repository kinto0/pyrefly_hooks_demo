# Approach 4: Stop Hook with Exit 2

## Configuration

A Stop hook in `.claude/settings.local.json` that runs pyrefly and exits with code 2 on failure.

```json
{
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "command",
        "command": "pyrefly check >&2 || exit 2",
        "timeout": 30
      }]
    }]
  }
}
```
