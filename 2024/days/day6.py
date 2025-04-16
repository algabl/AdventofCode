import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers
import re

day = helpers.get_current_day(__file__)
input = helpers.read_input(day)
sample = helpers.read_input(day, sample=True)


def countChar(char: str) -> int:
    total = 0
    for line in input:
        for char in line:
            if char == 'X':
                total += 1
    return total

def replaceCharacter(line_index: int, char_index: int, with_char: str, in_array):
    in_array[line_index] = in_array[line_index][:char_index] + with_char + in_array[line_index][char_index + 1:]

def mapNextMove(position, direction, in_array, part2: bool = False):
    line_index = position[1]
    char_index = position[0]
    current_char = in_array[line_index][char_index]
    
    # Determine if this is a turning point
    is_turning = False
    
    if part2:
        if direction == 'up' or direction == 'down':
            replacement_character = '|'
        elif direction == 'left' or direction == 'right':
            replacement_character = '-'
    else:
        replacement_character = 'X'
        
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

    # Check if out of bounds
    if potential_position[1] > len(in_array) - 1 or potential_position[1] < 0 or \
       potential_position[0] > len(in_array[0]) - 1 or potential_position[0] < 0:
        return potential_position, direction, False

    # Check if hitting obstacle
    if in_array[potential_position[1]][potential_position[0]] == '#' or in_array[potential_position[1]][potential_position[0]] == 'O':
        is_turning = True
        direction = potential_direction
    else:
        position = potential_position

    # Update the character at current position
    if part2:
        if is_turning and current_char != '+':
            replaceCharacter(line_index, char_index, '+', in_array)
        elif current_char != '+':
            replaceCharacter(line_index, char_index, replacement_character, in_array)
        
        next_position = getNextPosition(position, direction)
        
        # Check if out of bounds
         
        next_char = in_array[next_position[1]][next_position[0]]
        # Check for loop completion, also need to check if next move has already been visited
        if current_char == '+' and is_turning and (next_char == 'O' or next_char == '+' or next_char == '-' or next_char == '|'):
            return True

    return position, direction, True

def getNextPosition(position, direction):
    if direction == 'up':
        return position[0], position[1] - 1
    elif direction == 'right':
        return position[0] + 1, position[1]
    elif direction == 'down':
        return position[0], position[1] + 1
    elif direction == 'left':
        return position[0] - 1, position[1]

def findGuard(in_array):
    y = -1
    x = -1
    for index, line in enumerate(in_array):
        x = line.find('^')
        if x != -1:
            y = index
            break
    return [x, y]

def part1() -> int:
  
    total = 0

    # find guard
    guard_position = findGuard(input)
    direction = 'up'
    on_board = True
    while on_board:
        guard_position, direction, on_board = mapNextMove(guard_position, direction, input)

    # based on location and direction, map next move
    # mark visited locations with 'X'

    # count X's

    total = countChar('X')
    return total


# need:
# - way to place new obstruction
# - way to keep track of where the guard has been and in what direction. we could change the mapnextmove function to do this
# - when mapping next move and an obstacle is hit, check if a '+' has already been placed there.

def part2() -> int:
    from copy import deepcopy
    input = sample
    total = 0
    for line_index, line in enumerate(input):
        for char_index, char in enumerate(line):
            if input[line_index][char_index] == '.':
                if line_index == 6 and char_index == 3:
                    print("here")

                # Create a deep copy of the input
                test_input = deepcopy(input)
                replaceCharacter(line_index, char_index, 'O', test_input)
                guard_position = findGuard(test_input)
                direction = 'up'
                looping = False

                # Add a safety counter to prevent infinite loops
                max_steps = len(test_input) * len(test_input[0]) * 4
                steps = 0

                while not looping and steps < max_steps:
                    steps += 1
                    result = mapNextMove(guard_position, direction, test_input, True)
                    if result is True:  # Explicit check for True
                        looping = True
                        total += 1
                        print(f"Found a loop at {char_index}, {line_index}, total: {total}")
                        break
                    elif result[2] is False:  # Guard went off board
                        break
                    else:
                        guard_position, direction, _ = result

    return total




print(f"----- Day {day}: -----")
print(f"Part1: {part1()}")
print(f"Part2: {part2()}")

