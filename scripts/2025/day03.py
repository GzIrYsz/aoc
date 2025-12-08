import pathlib

SCRIPT = pathlib.Path(__file__)
SCRIPT_DIR = SCRIPT.parent
PROJECT_DIR = SCRIPT_DIR.parent.parent
DATA_DIR = PROJECT_DIR / "data" / SCRIPT_DIR.name
DATA_FILE = DATA_DIR / SCRIPT.with_suffix(".txt").name


def main():
    banks = []
    with open(DATA_FILE) as file:
        for line in file:
            bank = tuple([int(c) for c in line.strip()])
            banks.append(bank)

    sum_joltages = 0
    for bank in banks:
        n1 = bank[0]
        n2 = bank[1]
        for i in range(1, len(bank) - 1):
            if bank[i] > n1:
                n1 = bank[i]
                n2 = bank[i + 1]
            if bank[i + 1] > n2:
                n2 = bank[i + 1]
        sum_joltages += int(f"{n1}{n2}")
    print(f"Part One: {sum_joltages}")

    sum_joltages = 0
    for bank in banks:
        nums = list(bank[:12])
        for i in range(1, len(bank) - 11):
            for j in range(len(nums)):
                if bank[i + j] > nums[j]:
                    for k in range(j, len(nums)):
                        nums[k] = bank[i + k]
        nums = [str(n) for n in nums]
        sum_joltages += int(str.join("", nums))
    print(f"Part Two: {sum_joltages}")


if __name__ == '__main__':
    main()
