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
amount_safe = 0
amount_unsafe = 0

with open("Day2Problem1/input.txt", "r") as file:
    for index, line in enumerate(file):
        line = line.rstrip()
        reports.append(list(map(int, line.split())))

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
    else:
        amount_unsafe += 1
print('Amount safe:' + str(amount_safe))
print('Amount unsafe:' + str(amount_unsafe))
print('Total:' + str(len(reports)))

