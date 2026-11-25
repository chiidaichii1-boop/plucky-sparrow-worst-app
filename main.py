#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched: ChirpAlert.

Writes one sentence pitching the worst, most useless app imaginable
to <output dir>/entry.txt. Pure standard library, fully deterministic.
"""

import os

ENTRY = (
    # One clean sentence, 134 characters, well inside the 1-240 gate.
    "ChirpAlert texts you the instant a bird within 500 metres chirps, "
    "because in a world full of noise, no chirp should ever go unnoticed."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not (1 <= len(text) <= 240) or not text.strip():
        raise SystemExit("entry must be 1-240 non-whitespace characters")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
