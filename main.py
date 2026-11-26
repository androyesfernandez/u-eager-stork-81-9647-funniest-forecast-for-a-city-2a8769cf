#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't — entry program.

Writes the tournament-winning forecast line to /output/entry.txt:
exactly 87 bytes, no trailing newline.
"""

LINE = "Breezy Bottom: gusts of 12 umbrellas per hour, peaking at one airborne mailbox by noon."


def main() -> None:
    import os

    # Encode once, write exact bytes: no newline translation, no
    # accidental trailing newline, byte count == character count.
    payload = LINE.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(payload)
    assert len(payload) == 87, f"expected 87 bytes, got {len(payload)}"


if __name__ == "__main__":
    main()
