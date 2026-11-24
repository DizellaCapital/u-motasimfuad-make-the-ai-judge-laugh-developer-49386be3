#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses entry.

One original single-line excuse a developer gives when code breaks in
production (64 characters), written to /output/entry.txt. Deterministic:
the same line on every run, no network, no randomness, stdlib only.
"""

from pathlib import Path

LINE = "I only changed one line \u2014 turns out it was the load-bearing one."

MAX_CHARS = 200
OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"


def validate(line: str) -> str:
    """The gate needs 1-200 characters of real text, not only whitespace."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line is {len(line)} characters, must be 1-{MAX_CHARS}")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line, no embedded newlines")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("line must not contain control characters")
    return line


def main(argv: list[str] | None = None) -> None:
    text = validate(LINE)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(text + "\n", encoding="utf-8")
    # Read back what was written: the entry must be exactly the line,
    # nothing more, before the run can call itself done.
    written = OUT_FILE.read_text(encoding="utf-8")
    assert written == text + "\n", "entry.txt does not match the line"
    if argv and "--count" in argv:
        print(f"{len(text)} characters")


if __name__ == "__main__":
    main()
