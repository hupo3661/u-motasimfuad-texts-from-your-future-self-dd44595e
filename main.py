"""Texts From Your Future Self — one-line entry.

The writer's future self sends one text message back to the
present: a plant bought to become a plant person, dead in
eleven days, and the pot that somehow outlived it.

The joke is the reversal — the living thing dies, the container
thrives — told in the flat, slightly embarrassed voice of a
future self who has already had this argument with the past.

Prints that single text message, and nothing else.
"""

# The entry line, exactly as the judge reads it. Keep every word,
# comma and apostrophe untouched: entry.txt holds the same text,
# and the program's stdout must match it byte for byte.
LINE = "Hey, it's you from 2031. The plant you bought to \"become a plant person\" died in 11 days. We never speak of it. The pot, however, is thriving."


def main() -> None:
    # One print, one line, nothing else: no extra output, no files,
    # no stderr. The entry is judged on this stdout text alone, so
    # the program stays deliberately boring around the sentence.
    print(LINE)


if __name__ == "__main__":
    main()
