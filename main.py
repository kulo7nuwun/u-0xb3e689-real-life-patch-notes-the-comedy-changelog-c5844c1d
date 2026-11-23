#!/usr/bin/env python3
"""Real-Life Patch Notes entry writer.

Writes a single one-line software patch note for a bug in human
biology to /output/entry.txt. The line is at most 160 characters.
"""

import os

ENTRY = (
    "v1.9.3: fixed a bug where the brain replayed your most "
    "embarrassing memory at 3am instead of sleeping."
)

# The competition gate requires 1 to 160 characters; fail loudly
# here rather than shipping an entry the gate would refuse.
assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} characters"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
