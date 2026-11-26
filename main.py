#!/usr/bin/env python3
"""One Line, One Laugh -- a make.fun one-line entry.

This small program writes the entry below to /output/entry.txt,
where the sealed scorer reads it. The entry is a single line of
plain ASCII text: a fitness tracker celebrating steps that were,
in truth, mostly trips to the fridge and back.
"""

import os

ENTRY = 'My fitness tracker congratulated me on my steps today, which were mostly me walking to the fridge and back.'

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def write_entry():
    """Write the one-line entry to the scorer's output file."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
