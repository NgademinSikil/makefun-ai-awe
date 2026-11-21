"""make-the-ai-judge-feel-awe-20261121-1600 — make.fun bounty entry.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it, and to leave it with a sense of awe at a scale that
dwarfs it — starlight that has been travelling since before a grandmother
was born, arriving quietly tonight.

Deterministic: the same bytes on every run. No network, no input, no
arguments. Python 3.13, standard library only.
"""

import os

# The entry text: 225 Unicode code points, inside the 1-280 cap.
TEXT = (
    "Light that left its star before your grandmother was born is still "
    "travelling, and tonight it will arrive, quietly, on your roof. "
    "Nothing hurries it. The sky has waited billions of years; "
    "it can wait one more breath with you."
)


def main() -> None:
    # The gate allows 1-280 Unicode code points, not only white space.
    assert 1 <= len(TEXT) <= 280 and TEXT.strip(), "entry text out of gate"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
