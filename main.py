"""The Internet in One Word — make.fun entry.

Writes the single-word entry to /output/entry.txt (UTF-8, no
trailing newline). Python stdlib only, deterministic, no network.
"""

import os

ENTRY = "Doomscroll"


def main() -> None:
    assert 1 <= len(ENTRY) <= 30, "entry must be 1-30 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

# Entry: "Doomscroll" — one word, 10 characters, no trailing newline.
