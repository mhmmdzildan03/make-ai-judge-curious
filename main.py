#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

The text is a small, calm scene meant to leave a reader curious:
a man who ferries an empty chair across a river every morning,
and the gentle mystery of who it might be for.
"""
import os

TEXT = (
    "Every dawn, Tomas rows an empty chair across the still river. "
    "On the far bank, he sets it facing the water and pours a second "
    "cup of tea beside his own. He never says who it is for. "
    "He only smiles: 'She likes to arrive unhurried. "
    "She has never once been late.'"
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
