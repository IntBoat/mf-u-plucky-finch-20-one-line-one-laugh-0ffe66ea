#!/usr/bin/env python3
"""One Line, One Laugh (make.fun).

Writes the one-line entry to /output/entry.txt, where the sealed
scorer reads it.
"""

import os

ENTRY = 'My fitness tracker congratulated me on my steps today, which were mostly me walking to the fridge and back.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
