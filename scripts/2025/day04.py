import pathlib

SCRIPT = pathlib.Path(__file__)
SCRIPT_DIR = SCRIPT.parent
PROJECT_DIR = SCRIPT_DIR.parent.parent
DATA_DIR = PROJECT_DIR / "data" / SCRIPT_DIR.name
DATA_FILE = DATA_DIR / SCRIPT.with_suffix(".txt").name


def main():
    paper_grid = []
    with open(DATA_FILE) as file:
        for line in file:
            paper_grid.append(list(line.strip()))

    num_paper_rolls_movable = 0
    directions = [-1, 0, 1]
    for i in range(len(paper_grid)):
        for j in range(len(paper_grid[i])):
            if not paper_grid[i][j] == "@":
                continue
            adjacent_paper_rolls = 0
            for di in directions:
                if i + di < 0 or i + di >= len(paper_grid):
                    continue
                for dj in directions:
                    if j + dj < 0 or j + dj >= len(paper_grid[i]):
                        continue
                    if di == 0 and dj == 0:
                        continue
                    if paper_grid[i + di][j + dj] == "@":
                        adjacent_paper_rolls += 1
            if adjacent_paper_rolls < 4:
                num_paper_rolls_movable += 1
    print(f"Part One: {num_paper_rolls_movable}")

    num_paper_rolls_removable = 0
    changed = True
    while changed:
        changed = False
        for i in range(len(paper_grid)):
            for j in range(len(paper_grid[i])):
                if not paper_grid[i][j] == "@":
                    continue
                adjacent_paper_rolls = 0
                for di in directions:
                    if i + di < 0 or i + di >= len(paper_grid):
                        continue
                    for dj in directions:
                        if j + dj < 0 or j + dj >= len(paper_grid[i]):
                            continue
                        if di == 0 and dj == 0:
                            continue
                        if paper_grid[i + di][j + dj] == "@":
                            adjacent_paper_rolls += 1
                if adjacent_paper_rolls < 4:
                    paper_grid[i][j] = "."
                    changed = True
                    num_paper_rolls_removable += 1
    print(f"Part Two: {num_paper_rolls_removable}")


if __name__ == '__main__':
    main()
