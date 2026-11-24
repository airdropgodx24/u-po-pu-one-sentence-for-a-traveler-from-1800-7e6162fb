# One Sentence for a Traveler from 1800.
# This program writes a single sentence to entry.txt in the output
# directory (MAKEFUN_OUTPUT_DIR when set, else /output). The sentence
# explains the modern internet using only things a person from 1800
# already knows: post offices, libraries, roads, letters, books, towns.

import os

SENTENCE = "Picture every post office and library on earth joined by one road, so a letter reaches any town in a blink and any book stands open on your own table, day or night."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
