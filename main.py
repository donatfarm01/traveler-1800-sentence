"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler from 1800, using only images and words they
could already picture: post offices, libraries, market squares, roads.
"""

import os

SENTENCE = (
    "Picture every post office, library, and market square in the world "
    "joined by roads of light, so any letter, book, or voice reaches any "
    "door in a blink, and any door can answer back."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = SENTENCE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
