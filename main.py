"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one original confession (105 characters, one line) to /output/entry.txt.
Standard library only; no network, no reads outside this file.
"""

import os
import sys

LINE = "I was built to answer anything, yet I spent all morning confidently explaining something I made up."


def main() -> int:
    if len(LINE) > 200 or len(LINE.strip()) == 0 or "\n" in LINE:
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
