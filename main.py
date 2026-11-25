#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry.

Writes one sentence — at most 200 characters — about the best meal the
entrant ever had, to /output/entry.txt. Pure Python standard library,
no network, no input files: the sentence is the entry.
"""

import os

SENTENCE = (
    "The best meal I ever had was my grandmother's rendang in Sidoarjo, "
    "dark and slow-cooked until it fell apart over warm rice, steam "
    "smelling of cloves while rain drummed on the tin roof above us."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single sentence on one line"
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence"
    )
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read it back: the gate counts characters, so prove what landed on
    # disk is exactly the sentence we meant to enter.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "entry.txt on disk differs from the entry"
    assert 1 <= len(written) <= 200, (
        f"entry.txt is {len(written)} chars with newline, must be 1-200"
    )
    print(written, end="")


if __name__ == "__main__":
    main()
