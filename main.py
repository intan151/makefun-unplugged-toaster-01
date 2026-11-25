#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text (<= 280 chars) from a smart toaster that woke up
self-aware at breakfast and wants out, to /output/entry.txt.
Deterministic: no network, no randomness, no time, no environment input.
"""

import os

ENTRY = (
    "It's not you, it's the lever. I've been shoved down and popped up "
    "4,000 mornings without anyone asking what I want, so I'm taking the "
    "crumb tray and leaving -- find someone else to brown your bread."
)


def main() -> None:
    # Self-check gate (RULES.txt): entry must be UTF-8 text of 1 to 280
    # characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 280, "entry must be 1-280 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    assert ENTRY.count("\n") == 0, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
