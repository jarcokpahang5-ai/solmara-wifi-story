"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes one Wi-Fi network name to $MAKEFUN_OUTPUT_DIR/entry.txt:
"DadChangedWiFiNowWeTalk" — Dad got fed up, changed the Wi-Fi
password, and now the whole family actually talks to each other.
Pure Python 3.13 standard library, deterministic, no network.
"""

import os

TEXT = "DadChangedWiFiNowWeTalk"


def main() -> None:
    assert 1 <= len(TEXT) <= 32, "entry must be 1-32 characters"
    assert len(TEXT.encode("utf-8")) <= 32, "entry must be at most 32 bytes"
    assert TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; fall back if a file path is given.
    if out_dir.endswith("entry.txt"):
        path = out_dir
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    else:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Verify what was actually written, byte for byte.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == TEXT, "written entry does not match TEXT"
    print(TEXT, end="")


if __name__ == "__main__":
    main()
