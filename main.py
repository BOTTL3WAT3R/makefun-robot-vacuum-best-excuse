#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one line, the vacuum's own excuse for missing a spot, to
/output/entry.txt. The line is deadpan machine logic: the vacuum
insists it did not miss the spot at all; it visited, classified the
dust as load-bearing, and respectfully routed around it.
"""

import os

ENTRY = (
    "I did not miss that spot. I bumped into it six times, classified "
    "the dust as load-bearing, and respectfully routed around it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
