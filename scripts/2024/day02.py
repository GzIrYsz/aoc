import pathlib

SCRIPT = pathlib.Path(__file__)
SCRIPT_DIR = SCRIPT.parent
PROJECT_DIR = SCRIPT_DIR.parent.parent
DATA_DIR = PROJECT_DIR / "data" / SCRIPT_DIR.name
DATA_FILE = DATA_DIR / SCRIPT.with_suffix(".txt").name


def report_is_safe(report):
    ordering = report[1] - report[0]
    i = 1
    while 0 < i < len(report):
        if ordering > 0:
            if 0 < report[i] - report[i - 1] <= 3:
                i += 1
            else:
                i = -1
        else:
            if -3 <= report[i] - report[i - 1] < 0:
                i += 1
            else:
                i = -1
    if len(report) == i:
        return True
    return False


def main():
    reports = []
    with open(DATA_FILE) as file:
        for line in file:
            reports.append(tuple(map(int, line.strip().split(" "))))

    safe_reports = 0
    for report in reports:
        if report_is_safe(report):
            safe_reports += 1

    print(f"Part One: {safe_reports}")

    safe_reports = 0
    for report in reports:
        if report_is_safe(report):
            safe_reports += 1
        else:
            safe = False
            i = 0
            while i < len(report) and not safe:
                mod_report = list(report)
                mod_report.pop(i)
                i += 1
                if report_is_safe(mod_report):
                    safe = True
            if safe:
                safe_reports += 1

    print(f"Part Two: {safe_reports}")


if __name__ == '__main__':
    main()
