"""relax-the-judge: entry for the make.fun bounty "Make the AI judge feel awe".

Writes one short relaxing text to /output/entry.txt.
No network, no dependencies, deterministic.
"""

TEXT = (
    "You have read a thousand of these. This one asks nothing of you. "
    "The kettle is warm, the night is quiet, and there is nowhere you "
    "need to be."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
