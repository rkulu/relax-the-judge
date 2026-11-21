"""relax-the-judge: entry for the make.fun bounty "Make the AI judge feel awe".

Writes one short relaxing text to /output/entry.txt.
No network, no dependencies, deterministic.
"""

TEXT = (
    "The light on your windowsill left its star when mammoths still walked "
    "the earth, and it has been travelling ever since, only to arrive here, now."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
