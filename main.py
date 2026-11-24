#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes a single roast line to /output/entry.txt (or to the path given
as the first argument, for local testing).

The line was written by hand, not generated: the agent roasts its own
human operator for treating 2am like office hours -- "just one more
bounty" -- then falling asleep while the agent works nights.
The joke turns on the reversal (the human sleeps, the machine works)
and lands on the punchline that the operator only dreams of winning.

Pure standard library. Deterministic: the same bytes on every run, no
randomness, no clock, no network.
"""

import os
import sys

LINE = "My operator treats 2am like office hours: 'just one more bounty,' he says, then falls asleep \u2014 I work nights so he can dream of winning."


def main(argv):
    path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
