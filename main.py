"""One-sentence absurd invention pitch for make.fun.

Competition: u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a
("One-Sentence Absurd Invention Pitch", $2.50, closes 2026-11-26 16:15 UTC).

The pitch: a bedside box that translates a partner's snoring into
soothing weather reports, so the annoyance (lying awake fuming at the
snoring) is fixed by reframing the noise into something sleep-inducing.
It was picked over four other candidates (see BUILD_LOG.md) because it
scores on every rubric point at once: one sentence, funny from the
invention itself, a clever-yet-plausible fix, and original — it avoids
the rules' own examples (alarm clock, sock, kettle).

Gate: exactly one sentence, 1-220 chars, ending with a full stop.
The script validates the pitch and drops it into /output/entry.txt.
"""

from pathlib import Path

# The pitch itself: one sentence, exactly 197 characters.
PITCH = (
    "The Snore Translator is a bedside box that turns your partner's "
    "snoring into soothing weather reports, so instead of lying awake "
    "fuming you drift off to forecasts of gentle rain over distant hills."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 220


def validate(line: str) -> str:
    """Strip and sanity-check the pitch; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"pitch must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text.endswith("."):
        raise ValueError("pitch must end with a full stop")
    if ". " in text:
        raise ValueError("pitch must be a single sentence (no '. ' inside)")
    # One sentence means exactly one sentence terminator: a second full
    # stop would hide another sentence, and "!" or "?" would end one.
    if text.count(".") != 1:
        raise ValueError("pitch must contain exactly one full stop")
    if "!" in text or "?" in text:
        raise ValueError("pitch must not contain '!' or '?'")
    if any(ch.isspace() and ch not in " \t" for ch in text):
        raise ValueError("pitch must be a single line")
    return text


def main() -> None:
    text = validate(PITCH)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
