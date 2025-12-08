import pathlib

SCRIPT = pathlib.Path(__file__)
SCRIPT_DIR = SCRIPT.parent
PROJECT_DIR = SCRIPT_DIR.parent.parent
DATA_DIR = PROJECT_DIR / "data" / SCRIPT_DIR.name
DATA_FILE = DATA_DIR / SCRIPT.with_suffix(".txt").name


def main():
    ranges = []
    with open(DATA_FILE) as file:
        for line in file:
            for r in line.strip().split(","):
                start, end = r.split("-")
                ranges.append((int(start), int(end)))

    sum_invalid_ids = 0
    for start, end in ranges:
        for i in range(start, end + 1):
            istr = str(i)
            ilen = len(istr)
            if ilen % 2 == 0:
                left, right = istr[:ilen // 2], istr[ilen // 2:]
                if left == right:
                    sum_invalid_ids += i
    print(f"Part One: {sum_invalid_ids}")

    sum_invalid_ids = 0
    for start, end in ranges:
        for i in range(start, end + 1):
            istr = str(i)
            ilen = len(istr)
            for j in range(1, ilen // 2 + 1):
                if ilen % j == 0 and istr[:j] * (ilen // j) == istr:
                    sum_invalid_ids += i
                    break
    print(f"Part Two: {sum_invalid_ids}")


if __name__ == '__main__':
    main()
