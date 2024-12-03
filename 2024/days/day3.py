import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers
import re

day = helpers.get_current_day(__file__)
input = helpers.read_input(day, False)
# extracts the numbers 
def extractProductFrom(input: str) -> int:
    left_int = int(input.split('(')[1].split(',')[0])
    right_int = int(input.split(',')[1].split(')')[0])
    return left_int * right_int

def part1(input: str) -> int:
    result = 0
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)
    for match in matches:
        result += extractProductFrom(match)
    return result   

def part2(input: str) -> int:
    result = 0
    conditionals = re.split(r"(\bdo\b\(\)|\bdon't\b\(\))", input)
    do = True
    for entry in conditionals:
        if entry == "do()":
            do = True
        elif entry == "don't()":
            do = False
        elif do:
            result += part1(entry)
    return result

print(f"----- Day {day}: -----")
print(f"Part1: {part1(input)}")
print(f"Part2: {part2(input)}")