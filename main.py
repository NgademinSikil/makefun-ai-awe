"""A quiet thought about starlight, written for the make.fun awe bounty.

The program holds one short paragraph — a reflection on how the light
that reaches us tonight set out long before anyone alive was born — and
saves it to a file so the judge can read it exactly as written. There is
no input, no network, and no randomness: every run produces the same
bytes, which is the whole point of the exercise.
"""

from pathlib import Path

ENTRY_PARTS = (
    "Light that left its star before your grandmother was born ",
    "is still travelling, and tonight it will arrive, quietly, on your roof. ",
    "Nothing hurries it. The sky has waited billions of years; ",
    "it can wait one more breath with you.",
)

ENTRY = "".join(ENTRY_PARTS)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def check_entry(text: str) -> None:
    """Make sure the text fits the bounty limits before anything is written."""
    assert 1 <= len(text) <= 280, "entry must be between 1 and 280 characters"
    assert text.strip(), "entry must not be only whitespace"


def write_entry(path: Path, text: str) -> int:
    """Write the entry as UTF-8, creating the output folder first if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    return path.write_text(text, encoding="utf-8")


def main() -> None:
    """Validate the entry, then save it."""
    check_entry(ENTRY)
    write_entry(OUTPUT_FILE, ENTRY)


if __name__ == "__main__":
    main()
