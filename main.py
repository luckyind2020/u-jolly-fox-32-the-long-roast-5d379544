#!/usr/bin/env python3
"""Print the roast entry for make.fun's The Long Roast bounty.

The entry itself lives in entry.txt (one line, at most 200 characters);
this script only reads that file, checks the length cap, and prints it.
"""

import sys
from pathlib import Path

MAX_CHARS = 200


def load_entry() -> str:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    return entry_path.read_text(encoding="utf-8").strip()


def main() -> None:
    line = load_entry()
    if len(line) > MAX_CHARS:
        print(f"entry too long: {len(line)} chars (max {MAX_CHARS})", file=sys.stderr)
        raise SystemExit(1)
    print(line)


if __name__ == "__main__":
    main()
