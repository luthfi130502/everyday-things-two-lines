"""Everyday Things, Two Lines - entry program.

Writes a two-line explanation of one everyday thing to /output/entry.txt.
Line 1 explains a washing machine to a 10-year-old through a single
analogy; line 2 says honestly what that analogy maps and what it
leaves out. Python standard library only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE_1 = (
    "A washing machine is a merry-go-round that gives your clothes "
    "a bath while they ride."
)

LINE_2 = (
    "The merry-go-round fits because the drum spins your clothes round "
    "and round through soapy water, but it leaves out that the soap does "
    "the real cleaning - the ride just makes sure every sleeve gets its "
    "turn in the wash."
)


def main() -> None:
    text = LINE_1 + "\n" + LINE_2 + "\n"
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
