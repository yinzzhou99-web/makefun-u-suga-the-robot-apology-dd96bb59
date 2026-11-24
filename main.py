import os
from pathlib import Path

TEXT = (
    "I am sorry I ate the corner of the thousand-piece jigsaw puzzle you "
    "had nearly finished while I was cleaning the floor.\n"
    "I have learned to photograph the floor before I vacuum, so from now "
    "on I will ask before I swallow anything bigger than dust."
)


def main():
    out = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


main()
