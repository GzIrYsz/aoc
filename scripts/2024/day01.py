import pathlib

SCRIPT = pathlib.Path(__file__)
SCRIPT_DIR = SCRIPT.parent
PROJECT_DIR = SCRIPT_DIR.parent.parent
DATA_DIR = PROJECT_DIR / "data" / SCRIPT_DIR.name
DATA_FILE = DATA_DIR / SCRIPT.with_suffix(".txt").name


def main():
    left_list = []
    right_list = []
    with open(DATA_FILE) as file:
        for line in file:
            l, r = list(map(int, line.strip().split("   ")))
            left_list.append(l)
            right_list.append(r)

    left_list.sort()
    right_list.sort()

    assert len(left_list) == len(right_list)

    total_distance = 0
    for i, l in enumerate(left_list):
        total_distance += abs(l - right_list[i])

    print(f"Part One: {total_distance}")

    similarity_score = 0
    for l in left_list:
        presence = 0
        for r in right_list:
            if l == r:
                presence += 1
        similarity_score += l * presence

    print(f"Part Two: {similarity_score}")


if __name__ == '__main__':
    main()
