import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers
import re

day = helpers.get_current_day(__file__)
input = helpers.read_input(day)

xmas = 'XMAS'

def checkAround(line_index: int, char_index: int, for_char: str, limit: int = 3): 
    offsets = []

    for h_offset in range(-1, 2):
        for v_offset in range(-1, 2):
            if (line_index + (v_offset * limit)) < 0 or (line_index + (v_offset * limit)) > len(input) - 1 or (char_index + (h_offset * limit)) < 0 or (char_index + (h_offset * limit)) > len(input[0]) - 1:
                continue
            if check(line_index + v_offset, char_index + h_offset, for_char):
                offsets.append((h_offset, v_offset))
    if len(offsets) > 0:
        return True, offsets
    else:
        return False, offsets

def check(line_index: int, char_index: int, for_char: str):
    if line_index > len(input) - 1 or char_index > len(input[line_index]) - 1: 
        return False
    return input[line_index][char_index] == for_char



def part1():
    times = 0
    for line_index, line in enumerate(input):
        for char_index, char in enumerate(line):
            if char == 'X':
                m_found, offsets = checkAround(line_index, char_index, 'M')
                if m_found:
                    for h_offset, v_offset in offsets:
                        if check(line_index + (v_offset * 2), char_index + (h_offset * 2), 'A') and check(line_index + (v_offset * 3), char_index + (h_offset * 3), 'S'):
                            times += 1
    return times

def part2():
    times = 0

    for line_index, line in enumerate(input):
        for char_index, char in enumerate(line):
            # find a
            # then, look for M diagonally
            # if found, look for another M with only one of the same offsets
            # if 2nd m found, look for S's in the diagonal offsets that the M's do not share
            if char == 'A':
                m_found, offsets = checkAround(line_index, char_index, 'M', 1)

                valid_offsets = []

                for h_offset, v_offset in offsets:
                    if abs(h_offset) == 1 and abs(v_offset) == 1:
                        valid_offsets.append((h_offset, v_offset))

                if len(valid_offsets) == 2:
                    if valid_offsets[0][0] == valid_offsets[1][0]:
                        shared_m_offset = valid_offsets[0][0]
                        # both m's are in same column, we then check for S's in other column
                        if check(line_index - 1, char_index + (shared_m_offset * -1), 'S') and check(line_index + 1, char_index + (shared_m_offset * -1), 'S'):
                            times += 1
                    elif valid_offsets[0][1] == valid_offsets[1][1]:
                        shared_m_offset = valid_offsets[0][1]
                        # both m's are in same row, we then check for S's in other row
                        if check(line_index + (shared_m_offset * -1), char_index - 1, 'S') and check(line_index + (shared_m_offset * -1), char_index + 1, 'S'):
                            times += 1
                             

    return times

print(f"----- Day {day}: -----")
print(f"Part1: {part1()}")
print(f"Part2: {part2()}")