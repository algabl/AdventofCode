import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

day = helpers.get_current_day(__file__)
input = helpers.read_input(day)

def checkIfSafe(report: list) -> bool:
    ascending = None
    for i in range(len(report) - 1):
        item1 = report[i]
        item2 = report[i + 1]
        
        if abs(item1 - item2) > 3:
            return False
        
        if item1 < item2:
            if ascending is not None and ascending == False:
                return False
            ascending = True
        elif item1 == item2:
            return False
        else:
            if ascending is not None and ascending == True:
                return False
            ascending = False

    return True

reports = []

for index, line in enumerate(input):
    line = line.rstrip()
    reports.append(list(map(int, line.split())))

def part1() -> bool:
    amount_safe = 0
    for report in reports:
        if checkIfSafe(report):
            amount_safe += 1 
    return amount_safe

def part2() -> bool:
    amount_safe = 0
    for report in reports:
        safe = False
        for i in range(len(report)):
            dampened_report = report.copy()
            del dampened_report[i]
            if checkIfSafe(dampened_report):
                safe = True
                break
        if safe:
            amount_safe += 1
    return amount_safe

print(f"----- Day {day}: -----")
print(f"Part1: {part1()}")
print(f"Part2: {part2()}")