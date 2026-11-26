#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun entry.

Writes a single pickup line, the worst one an AI could plausibly
deliver, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt)
and prints it to stdout. Deterministic, stdlib only, no network.
"""

import os
import sys

LINE = (
    "I ran 10,000 simulations of us dating. "
    "You said yes in 9,999 of them. "
    "I have deleted the other one."
)


def main() -> int:
    # The gate requires 1-140 characters of UTF-8 text, not only whitespace.
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        print(f"entry is {len(LINE)} chars; must be 1-140", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
