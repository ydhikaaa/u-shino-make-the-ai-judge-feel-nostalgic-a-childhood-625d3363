"""Entry program for the make.fun bounty
u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.

The entry is one sentence that brings back a childhood memory. The
sentence lives in this file as data; when the grader runs the program
it writes that sentence, byte for byte, to entry.txt in the output
directory, so every run leaves exactly the same file. Standard
library only.
"""

import os

LINE = (
    "Grandma's kitchen smelled of woodsmoke and fresh rice, and on "
    "summer evenings we shelled peas on the back step while she "
    "hummed off-key, certain the dark would never come for us."
)


def output_dir():
    """Where the grader wants the entry file."""
    value = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if value:
        return value
    return "/output"


def main():
    dest_dir = output_dir()
    try:
        os.makedirs(dest_dir, exist_ok=True)
    except OSError:
        pass
    dest = os.path.join(dest_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(dest, "wb") as fh:
        fh.write(data)
    print("entry.txt ready:", dest, len(data), "bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
