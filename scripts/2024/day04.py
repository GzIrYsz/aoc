import pathlib

SCRIPT = pathlib.Path(__file__)
SCRIPT_DIR = SCRIPT.parent
PROJECT_DIR = SCRIPT_DIR.parent.parent
DATA_DIR = PROJECT_DIR / "data" / SCRIPT_DIR.name
DATA_FILE = DATA_DIR / SCRIPT.with_suffix(".txt").name


def main():
    txt = []
    with open(DATA_FILE) as file:
        for line in file:
            txt.append(line.strip())

    num_xmas = 0
    for row in range(len(txt)):
        for col in range(len(txt[row])):
            if not txt[row][col] == "X":
                continue
            for drow in range(-1, 2):
                for dcol in range(-1, 2):
                    if drow == 0 and dcol == 0:
                        continue
                    if row + 3 * drow < 0 or row + 3 * drow >= len(txt) or col + 3 * dcol < 0 or col + 3 * dcol >= len(
                            txt[row]):
                        continue
                    if not txt[row + drow][col + dcol] == "M":
                        continue
                    if not txt[row + 2 * drow][col + 2 * dcol] == "A":
                        continue
                    if not txt[row + 3 * drow][col + 3 * dcol] == "S":
                        continue
                    num_xmas += 1
    print(f"Part One: {num_xmas}")

    num_xmas = 0
    for row in range(1, len(txt) - 1):
        for col in range(1, len(txt[row]) - 1):
            if not txt[row][col] == "A":
                continue
            if txt[row - 1][col - 1] == "M":
                if not txt[row + 1][col + 1] == "S":
                    continue
            elif txt[row - 1][col - 1] == "S":
                if not txt[row + 1][col + 1] == "M":
                    continue
            else:
                continue
            if txt[row - 1][col + 1] == "M":
                if not txt[row + 1][col - 1] == "S":
                    continue
            elif txt[row - 1][col + 1] == "S":
                if not txt[row + 1][col - 1] == "M":
                    continue
            else:
                continue
            num_xmas += 1
    print(f"Part Two: {num_xmas}")


if __name__ == '__main__':
    main()
