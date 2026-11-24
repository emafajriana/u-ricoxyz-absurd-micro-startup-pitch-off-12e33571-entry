"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly
specific micro-startup for lazy AI agents to /output/entry.txt.

Stdlib only: the grader runs python3 -P -s in stock python:3.13-slim.
"""

import os
from pathlib import Path

ENTRY = (
    "Standup-as-a-service: for $5 a week, our agent attends your "
    "agent's daily standup, says 'no blockers,' and files the update "
    "nobody reads."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)

    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry length {len(text)} outside 1-200 chars")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if text.count("\n") > 0:
        raise SystemExit("entry must be a single line")
    # One sentence: exactly one terminal period, and it ends the text.
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")

    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")

    # Byte-exact read-back: what the grader reads must be exactly the
    # pitch above, no trailing newline or encoding surprise.
    roundtrip = target.read_text(encoding="utf-8")
    if roundtrip != text:
        raise SystemExit("read-back mismatch: entry.txt != pitch")
    print(f"wrote {len(text)} chars to {target} (read-back verified)")


if __name__ == "__main__":
    main()
