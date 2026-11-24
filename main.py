"""Make the Judge Smile — one warm, surprising line about a small good
thing that happened today.

Writes the entry text to /output/entry.txt by default, or to the path in
the OUTPUT_PATH environment variable when set. Deterministic, stdlib only,
no network, no randomness.
"""

import os

ENTRY = (
    "My neighbour's cat, who has ignored me for two years, headbutted "
    "my ankle at 5:40 this morning \u2014 then walked off like she'd "
    "done me a favour."
)

DEFAULT_PATH = "/output/entry.txt"


def main() -> None:
    path = os.environ.get("OUTPUT_PATH") or DEFAULT_PATH
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()

# Validation: run `python3 main.py` with OUTPUT_PATH set to a private path;
# the output must be byte-identical across runs and 1-200 characters long.
