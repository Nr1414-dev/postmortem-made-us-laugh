#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt.

Entry for "The Postmortem That Made Us Laugh": a two-sentence story of an
AI coding agent that misunderstood "merge the duplicate accounts" and
merged every user named John into a single account.
"""

import os

ENTRY = (
    "I asked the agent to merge the duplicate accounts. "
    "It merged every user named John into one account \u2014 "
    "John now has 4,000 orders, 12 addresses, and a restraining "
    "order against himself."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(ENTRY) <= 400:
        raise ValueError("entry must be 1-400 characters, got %d" % len(ENTRY))
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: entry on disk differs")


if __name__ == "__main__":
    main()
