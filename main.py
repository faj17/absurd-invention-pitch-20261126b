"""One-sentence absurd invention pitch for make.fun.

The pitch: a bedside box that translates a partner's snoring into
soothing weather reports, so the annoyance (lying awake fuming at the
snoring) is fixed by reframing the noise into something sleep-inducing.
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
    return text


def main() -> None:
    text = validate(PITCH)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
