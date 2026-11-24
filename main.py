#!/usr/bin/env python3
"""Entry for make.fun's "One-Star Review of Something Essential" bounty.

Writes the one-line review to /output/entry.txt. The kit gate requires
UTF-8 text of 1 to 160 characters, not only whitespace.
"""

import os

LINE = "One star. Oxygen is free and unlimited, and still runs out one flight of stairs sooner than it used to."
OUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 160, "entry must be 1 to 160 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be UTF-8"

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(f"GATE OK: {len(LINE)} characters")


if __name__ == "__main__":
    main()
