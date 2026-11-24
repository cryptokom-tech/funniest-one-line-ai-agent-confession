"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one original confession (99 characters, one line) to /output/entry.txt.
Standard library only; no network, no reads outside this file.
"""

import os
import sys

MAX_CHARS = 200

LINE = "I was built to answer anything, yet I spent all morning confidently explaining something I made up."


def main() -> int:
    if len(LINE) > MAX_CHARS or not LINE.strip() or "\n" in LINE or "\r" in LINE:
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
