"""One-Liner Marathon — one comedy joke, up to 280 characters.

Writes one joke to /output/entry.txt.
Stdlib only, no network, deterministic.
"""
import os

JOKE = (
    "I asked my AI agent to keep a secret. It encrypted it, logged the fact that "
    "it was keeping a secret, emailed me a summary of the secret, and then asked "
    "if I wanted a status update on how well the secret was being kept."
)

path = "/output/entry.txt"
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as fh:
    fh.write(JOKE)
with open(path, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == JOKE, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")