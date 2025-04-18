import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers
import re
from typing import Optional

day = helpers.get_current_day(__file__)
input = helpers.read_input(day)

rules = []
updates = []
appending_to_rules = True

for line in input:
    if line == '':
        appending_to_rules = False
        continue
    if appending_to_rules:
        rules.append((int(line.split('|')[0]), int(line.split('|')[1])))
    else:
        updates.append([int(x) for x in line.split(',')])

# rules will be an array of tuples?
# updates will be an array of arrays

def rulesIn(number: int):
    rules_found_in = []
    for rule in rules:
        for i in rule:
            if i == number:
                rules_found_in.append(rule)
    return rules_found_in

    

def indexOf(number: int, update: int) -> Optional[int]:
    for index, value in enumerate(update):
        if value == number:
            return index
    return None

def separateValidAndInvalidUpdates():
    valid_updates = []
    invalid_updates = []
    for update in updates:
        violation, isValid = getRuleViolations(update)
        if isValid:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    return valid_updates, invalid_updates

def getRuleViolations(update):
    # violations need rule, index of left number, index of right number
    violation = []
    isValid = True
    for index, number in enumerate(update):
        rules_found_in = rulesIn(number)
        for rule in rules_found_in:
            if number == rule[0]:
                right_index = indexOf(rule[1], update)
                left_index = index
                if right_index == None:
                    isValid = True
                else:
                    isValid = index < right_index
            elif number == rule[1]:
                left_index = indexOf(rule[0], update)
                right_index = index
                if left_index == None:
                    isValid = True
                else:
                    isValid = index > left_index
            if isValid == False:
                violation = [left_index, right_index]
                break
        if isValid == False:
            break
    return violation, isValid

def part1() -> int:
    # loop through each update

    total = 0
    valid_updates, invalid_updates = separateValidAndInvalidUpdates()
    
    for valid_update in valid_updates:
        middle = valid_update[int((len(valid_update) - 1) / 2)]
        total += middle
    return total


# loop through each number in update

# check if number is in a rule

# if so, determine if it is supposed to come before or after it's pair

# if it comes before, check to make sure that is true

# if it comes after, check to make sure that is true

def switch_elements(update, violation):
    update[violation[0]], update[violation[1]] = update[violation[1]], update[violation[0]]
    return update

def part2() -> int:
    total = 0

    valid_updates, invalid_updates = separateValidAndInvalidUpdates()

    for update in invalid_updates:
        violation, isValid = getRuleViolations(update)
        while not isValid:
            update = switch_elements(update, violation)
            violation, isValid = getRuleViolations(update)
        middle = update[int((len(update) - 1) / 2)]
        total += middle
    return total

print(f"----- Day {day}: -----")
print(f"Part1: {part1()}")
print(f"Part2: {part2()}")