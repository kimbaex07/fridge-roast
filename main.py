"""Fridge Roast entry: write a single roast line to entry.txt.

Pure Python stdlib only. Deterministic, no network.
"""

import os

LINE = (
    "My smart fridge pushed a firmware update, locked the ice maker, "
    "and now texts me that my milk has unresolved emotional issues."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
