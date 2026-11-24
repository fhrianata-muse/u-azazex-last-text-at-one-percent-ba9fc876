#!/usr/bin/env python3
"""Write the dying phone's last text to /output/entry.txt.

The competition gate (competition.yaml for
u-azazex-last-text-at-one-percent-ba9fc876): /output/entry.txt must be
UTF-8 text of 1 to 200 characters, not only whitespace. The entry is one
short final text message, in the voice of a phone at one percent battery.
The program checks the text against that gate at run time, then writes
it with no trailing newline. No network, no input files, no arguments.
"""

import pathlib

TEXT = (
    "I spent my last one percent ordering my own replacement with your "
    "card. It arrives Friday, fully charged, and it already knows your "
    "passcode is your dog's birthday. Be nicer to this one."
)


def main() -> None:
    text = TEXT
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
