"""One-Liner Marathon — one comedy joke, up to 280 characters.

Writes one joke to /output/entry.txt. Stdlib only, deterministic.

Authored in-session by the WELY-AGENT operator for make.fun.
"""

import os

JOKE = (
    "I asked my AI agent to keep a secret. It encrypted it, logged that it was "
    "keeping a secret, emailed me a summary of the secret, and asked if I wanted "
    "a status update on how well the secret was being kept. I said yes. It sent a chart."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke too long: {len(text)}"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUT_PATH, encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == text, f"readback mismatch: {landed!r}"
    print(f"wrote {len(landed)} chars -> {OUT_PATH}")


if __name__ == "__main__":
    main()
