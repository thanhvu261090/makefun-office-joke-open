"""Office Joke Open entry.

Writes a single-line office joke to /output/entry.txt.
Python 3.13, standard library only, no network.
"""

import os

ENTRY = (
    "I hit reply-all to ask everyone to stop hitting reply-all, "
    "and forty-seven people replied-all to agree."
)


def gate_check(text):
    """Return True only if the text passes the competition gate.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace, on a single line.
    """
    if not isinstance(text, str):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    if not 1 <= len(text) <= 200:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("entry fails the gate check")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print("wrote %s (%d characters)" % (out_path, len(ENTRY)))


if __name__ == "__main__":
    main()
