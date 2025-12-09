import pathlib

SCRIPT = pathlib.Path(__file__)
SCRIPT_DIR = SCRIPT.parent
PROJECT_DIR = SCRIPT_DIR.parent.parent
DATA_DIR = PROJECT_DIR / "data" / SCRIPT_DIR.name
DATA_FILE = DATA_DIR / SCRIPT.with_suffix(".txt").name


def main():
    lines = []
    with open(DATA_FILE) as file:
        for line in file:
            lines.append(line)

    lcopy = [line.strip() for line in lines]
    problems = [line.split() for line in lcopy]

    grand_total = 0
    for i in range(len(problems[0])):
        op = problems[-1][i]
        local_op = 1 if op == "*" else 0
        for j in range(len(problems) - 1):
            current_val = int(problems[j][i])
            if op == "*":
                local_op *= current_val
            elif op == "+":
                local_op += current_val
        grand_total += local_op
    print(f"Part One: {grand_total}")

    lcopy = [line.rstrip("\n")[::-1] for line in lines]
    problems = []
    calc = []
    for i, o in enumerate(lcopy[-1]):
        if lcopy[-1][max(0, i - 1)] != " ":
            continue
        n = ""
        for j in range(len(lcopy) - 1):
            n += lcopy[j][i]
        calc.append(n)
        if o != " ":
            calc.append(o)
            problems.append(calc)
            calc = []

    grand_total = 0
    for pb in problems:
        op = pb[-1]
        local_op = 1 if op == "*" else 0
        for i in range(len(pb) - 1):
            if op == "*":
                local_op *= int(pb[i].strip())
            elif op == "+":
                local_op += int(pb[i].strip())
        grand_total += local_op
    print(f"Part Two: {grand_total}")


if __name__ == '__main__':
    main()
