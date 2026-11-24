#!/usr/bin/env python3
"""Worst AI Advice entry.

Writes one line of the worst AI advice to /output/entry.txt.
"""

import os

LINE = "Pour water on a grease fire \u2014 the steam smothers the flames twice as fast."
# Why this line wins "worst": it is the single most infamous piece of
# terrible advice — confidently wrong, specific, and catastrophically
# dangerous (water on a grease fire explodes into a fireball), yet the
# fake mechanism ("steam smothers the flames") sounds just plausible
# enough that someone might believe it. That gap is the joke.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
