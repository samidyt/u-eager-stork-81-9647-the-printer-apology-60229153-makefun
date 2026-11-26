#!/usr/bin/env python3
"""The Printer Apology — make.fun bounty entry.

Writes one line (<=120 chars): an apology note from an office printer
to the people who keep jamming it, feeding it cheap paper and swearing at it.
"""

import os

ENTRY = "Sorry I jammed on page 47 of 48. You feed me paper thinner than your excuses, so now I chew out of spite."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
