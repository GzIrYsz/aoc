import pathlib

SCRIPT = pathlib.Path(__file__)
SCRIPT_DIR = SCRIPT.parent
PROJECT_DIR = SCRIPT_DIR.parent.parent
DATA_DIR = PROJECT_DIR / "data" / SCRIPT_DIR.name
DATA_FILE = DATA_DIR / SCRIPT.with_suffix(".txt").name


def main():
    fresh_ingredients_ranges = []
    ingredients = []
    with open(DATA_FILE) as file:
        save_ingredients_ranges = True
        for line in file:
            if not line.strip():
                save_ingredients_ranges = False
                continue
            if save_ingredients_ranges:
                start, end = line.strip().split("-")
                fresh_ingredients_ranges.append((int(start), int(end) + 1))
            else:
                ingredients.append(int(line.strip()))

    num_fresh_ingredients = 0
    for ingredient in ingredients:
        for start, end in fresh_ingredients_ranges:
            if start <= ingredient <= end:
                num_fresh_ingredients += 1
                break
    print(f"Part One: {num_fresh_ingredients}")

    num_possible_fresh_ingredients = 0
    last_range = None
    fresh_ingredients_ranges.sort()
    for start, end in fresh_ingredients_ranges:
        if last_range is None:
            last_range = (start, end)
        elif last_range[1] >= start:
            last_range = (last_range[0], max(last_range[1], end))
        else:
            num_possible_fresh_ingredients += last_range[1] - last_range[0]
            last_range = (start, end)
    num_possible_fresh_ingredients += last_range[1] - last_range[0]
    print(f"Part Two: {num_possible_fresh_ingredients}")


if __name__ == '__main__':
    main()
