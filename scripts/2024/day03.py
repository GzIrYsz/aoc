import pathlib
import re

SCRIPT = pathlib.Path(__file__)
SCRIPT_DIR = SCRIPT.parent
PROJECT_DIR = SCRIPT_DIR.parent.parent
DATA_DIR = PROJECT_DIR / "data" / SCRIPT_DIR.name
DATA_FILE = DATA_DIR / SCRIPT.with_suffix(".txt").name


def main():
    memory = DATA_FILE.read_text()
    mults = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", memory)
    mults = [int(a) * int(b) for a, b in mults]
    res = sum(mults)
    print(f"Part One: {res}")

    matcher = re.finditer(r"do\(\)|don't\(\)|mul\(([0-9]{1,3}),([0-9]{1,3})\)", memory)
    mults = []
    capture = True
    for match in matcher:
        token = match.group()
        if token == "don't()":
            capture = False
        elif token == "do()":
            capture = True
        elif capture:
            mults.append(int(match.group(1)) * int(match.group(2)))
    res = sum(mults)
    print(f"Part Two: {res}")


if __name__ == '__main__':
    main()
