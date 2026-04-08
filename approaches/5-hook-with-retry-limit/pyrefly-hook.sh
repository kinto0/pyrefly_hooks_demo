#!/bin/bash
# Pyrefly type-check hook with session-scoped retry limit.
# Reads session_id from Claude Code's stdin JSON for per-session counting.
# Gives Claude 3 attempts to fix type errors per session, then gives up.

MAX_RETRIES=3

# Read stdin JSON (Claude Code passes hook context)
INPUT=$(cat)

# Extract session_id from JSON using grep/sed (no jq dependency)
SESSION_ID=$(echo "$INPUT" | grep -o '"session_id":"[^"]*"' | sed 's/"session_id":"//;s/"//')

# Fallback if session_id not found
if [ -z "$SESSION_ID" ]; then
  SESSION_ID="global"
fi

COUNT_FILE="/tmp/.pyrefly-hook-count-$SESSION_ID"

# Read current retry count
count=$(cat "$COUNT_FILE" 2>/dev/null || echo 0)

# If we've exceeded retries for THIS session, give up
if [ "$count" -ge "$MAX_RETRIES" ]; then
  echo "WARNING: pyrefly errors remain after $MAX_RETRIES fix attempts in this session" >&2
  exit 0
fi

# Run pyrefly check
output=$(pyrefly check 2>&1)
rc=$?

if [ $rc -ne 0 ]; then
  # Type errors found — increment counter and block
  echo $((count + 1)) > "$COUNT_FILE"
  echo "$output" >&2
  exit 2
fi

# All clean — remove counter file
rm -f "$COUNT_FILE"
exit 0
