import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

day = helpers.get_current_day(__file__)
input = helpers.read_input(day)
sample = helpers.read_input(day, sample=True)

def allPossibleResults(values: list) -> list:
    if len(values) == 1:
        return values
    results = []
    for result in allPossibleResults(values[:-1]):
        results.append(result + values[-1])
        results.append(result * values[-1])
    return results

def day1(input=input) -> int:
    valid = 0
    for line in input:
        result = int(line.split(":")[0])
        values = list(map(int, line.split(":")[1].strip().split(" ")))
        if (result in allPossibleResults(values)):
            valid = valid + result
    return valid

def allPossibleResults2(values: list) -> list:
    if len(values) <= 1:
        return values
    results = []
    for result in allPossibleResults2(values[:-1]):
        results.append(result + values[-1])
        results.append(result * values[-1])
        results.append(int(str(result) + str(values[-1])))
    return results

def day2(input=input) -> int:
    valid = 0
    for line in input:
        result = int(line.split(":")[0])
        values = list(map(int, line.split(":")[1].strip().split(" ")))
        if (result in allPossibleResults2(values)):
            valid = valid + result
    return valid

print(day1(input))
print(day2(input))