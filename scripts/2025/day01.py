import pathlib

SCRIPT = pathlib.Path(__file__)
SCRIPT_DIR = SCRIPT.parent
PROJECT_DIR = SCRIPT_DIR.parent.parent
DATA_DIR = PROJECT_DIR / "data" / SCRIPT_DIR.name
DATA_FILE = DATA_DIR / SCRIPT.with_suffix(".txt").name


def main():
    rotations = []
    with open(DATA_FILE) as file:
        for line in file:
            side = -1 if line[0].strip() == "L" else 1
            distance = int(line[1:].strip())
            rotations.append((side, distance))

    dial_position = 50
    zeros = 0
    for side, distance in rotations:
        dial_position = (dial_position + side * distance) % 100
        if dial_position == 0:
            zeros += 1
    print(f"Part One: {zeros}")

    dial_position = 50
    zeros = 0
    for side, distance in rotations:
        div, mod = divmod(side * distance, side * 100)
        zeros += div
        if dial_position != 0 and dial_position + mod <= 0:
            zeros += 1
        elif dial_position + mod >= 100:
            zeros += 1
        dial_position = (dial_position + side * distance) % 100
    print(f"Part Two: {zeros}")


if __name__ == '__main__':
    main()
