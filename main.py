# u-kiencx-the-3am-commit-message-10bc7b35 entry (Python 3, standard library only):
# writes one fixed commit-message line to $MAKEFUN_OUTPUT_DIR/entry.txt
# (default /output). No trailing newline: the entry is exactly the line.
import os

LINE = "fix: squashed 38 commits into 'please work'. it didn't work. neither did i"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(path, line):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    write_entry(os.path.join(OUTPUT_DIR, "entry.txt"), LINE)
    assert 1 <= len(LINE) <= 139, "entry line must be 1-139 chars"


if __name__ == "__main__":
    main()
