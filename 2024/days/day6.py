import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers
import re

day = helpers.get_current_day(__file__)
input = helpers.read_input(day)


def countX() -> int:
    total = 0
    for line in input:
        for char in line:
            if char == 'X':
                total += 1
    return total

def part1() -> int:
    def findGuard():
        for index, line in enumerate(input):
            x = line.find('^')
            if x != -1:
                y = index
                break
        return [x, y]
    
    def mapNextMove(position, direction):
        line_index = position[1]
        char_index = position[0]
        input[line_index] = input[line_index][:char_index] + 'X' + input[line_index][char_index + 1:]
        if direction == 'up':
            potential_position = position[0], position[1] - 1
            potential_direction = 'right'
        elif direction == 'right':
            potential_position = position[0] + 1, position[1]
            potential_direction = 'down'
        elif direction == 'down':
            potential_position = position[0], position[1] + 1
            potential_direction = 'left'
        elif direction == 'left':
            potential_position = [position[0] - 1, position[1]]
            potential_direction = 'up'
        if potential_position[1] > len(input) or potential_position[1] < 0 or potential_position[0] > len(input[0]) or potential_position[0] < 0:
            return potential_position, direction, False
        if input[potential_position[1]][potential_position[0]] == '#':
            direction = potential_direction
        else:
            position = potential_position

        return position, direction, True

    total = 0

    # find guard
    guard_position = findGuard()
    direction = 'up'
    on_board = True
    while on_board:
        guard_position, direction, on_board = mapNextMove(guard_position, direction)

    

  

    # based on location and direction, map next move
    # mark visited locations with 'X'

    # count X's

    total = countX()
    return total

def part2() -> int:
    total = 0
    return total

print(f"----- Day {day}: -----")
print(f"Part1: {part1()}")
print(f"Part2: {part2()}")