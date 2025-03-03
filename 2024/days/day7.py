import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

day = helpers.get_current_day(__file__)
input = helpers.read_input(day)
sample = helpers.read_input(day, sample=True)

def canGetResultFromValues(result: int, values: list) -> int:
    return result in allPossibleResults(values)

def allPossibleResults(values: list) -> list:
    if len(values) == 1:
        return values
    results = []
    for result in allPossibleResults(values[:-1]):
        results.append(result + values[-1])
        results.append(result * values[-1])
    return results

def day1():
    valid = 0
    for line in input:
        result = int(line.split(":")[0])
        values = list(map(int, line.split(":")[1].strip().split(" ")))
        if (canGetResultFromValues(result, values)):
            valid = valid + result
    return valid


print(day1())