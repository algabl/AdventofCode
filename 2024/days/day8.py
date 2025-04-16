import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

day = helpers.get_current_day(__file__)
input = helpers.read_input(day)
sample = helpers.read_input(day, sample=True)

def distance_between(left, right):
    return left[0] - right[0] + left[1] - right[1]

class FrequencyRelationship:
    coordinates: tuple
    # offset from first item of tuple to second item of tuple
    offset: tuple

    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.offset= (coordinates[0][0] - coordinates[1][0], coordinates[0][1] - coordinates[1][1])

    def distance(self) -> int:
        return self.offset[0] + self.offset[1]
    
    def antinodes(self) -> tuple:
        antinode1 = (self.coordinates[0][0] + self.offset[0], self.coordinates[0][1] + self.offset[1])
        antinode2 = (self.coordinates[1][0] - self.offset[0], self.coordinates[1][1] - self.offset[1])
        return [antinode1, antinode2]
    # this function will return a list of all coordinates along the line between the two coordinates 
    # within the given width and height
    def expanded_antinodes(self, width, height) -> list:
        # while the current_antinode[0] is within the width and the current_antinode[1] is within the height
        # append the current_antinode to the list
        # then add the offset to the current_antinode
        (antinode1, antinode2) = self.antinodes()
        antinode_list = []
        current = antinode1
        while 0 <= current[0] < width and 0 <= current[1] < height:
            antinode_list.append(current)
            current = (current[0] + self.offset[0], current[1] + self.offset[1])
        current = antinode2
        while 0 <= current[0] < width and 0 <= current[1] < height:
            antinode_list.append(current)
            current = (current[0] - self.offset[0], current[1] - self.offset[1])

       # Also need to check in opposite directions from the original antenna positions
        current = (self.coordinates[0][0] - self.offset[0], self.coordinates[0][1] - self.offset[1])
        while 0 <= current[0] < width and 0 <= current[1] < height:
            antinode_list.append(current)
            current = (current[0] - self.offset[0], current[1] - self.offset[1])
        
        current = (self.coordinates[1][0] + self.offset[0], self.coordinates[1][1] + self.offset[1])
        while 0 <= current[0] < width and 0 <= current[1] < height:
            antinode_list.append(current)
            current = (current[0] + self.offset[0], current[1] + self.offset[1])
        
        return antinode_list



def part1(input=input) -> int:
    unique_antinode_map = {}
    antenna_map = {}
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char != '.':
                if char not in antenna_map:
                    antenna_map[char] = []
                else:
                    for coordinate in antenna_map[char]:
                        new_relationship = FrequencyRelationship((coordinate, (x,y)))
                        for antinode in new_relationship.antinodes():
                            if antinode[0] in range(len(line)) and antinode[1] in range(len(input)):
                                unique_antinode_map[str(antinode[0]) + ',' + str(antinode[1])] = True
                antenna_map[char].append((x,y))
    return len(unique_antinode_map)

def part2(input=input) -> int:
    unique_antinode_map = {}
    antenna_map = {}

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char != '.':
                if char not in antenna_map:
                    antenna_map[char] = []
                else:
                    for coordinate in antenna_map[char]:
                        new_relationship = FrequencyRelationship((coordinate, (x,y)))
                        for antinode in new_relationship.expanded_antinodes(len(line), len(input)):
                            if antinode[0] in range(len(line)) and antinode[1] in range(len(input)):
                                unique_antinode_map[str(antinode[0]) + ',' + str(antinode[1])] = True
                antenna_map[char].append((x,y))
    return len(unique_antinode_map)
print(part1(input))
print(part2(input))