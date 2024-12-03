import sys
sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

day = helpers.get_current_day(__file__)
input = helpers.read_input(day)

list1 = []
list2 = []
for index, line in enumerate(input):
    line = line.rstrip()
    value1, value2 = line.split("   ")
    list1.append(int(value1))
    list2.append(int(value2))
list1.sort()
list2.sort()

def part1() -> int:
    distance = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])
    return distance
    
def part2() -> int:
    similarity_score = 0
    for i in range(len(list1)):
        j = 0
        times_in_list_2 = 0
        while list1[i] >= list2[j]:
            j += 1
        
            if list1[i] == list2[j]:
                times_in_list_2 += 1

        similarity_score = similarity_score + (list1[i] * times_in_list_2)
    return similarity_score

print(f"----- Day {day}: -----")
print(f"Part1: {part1()}")
print(f"Part2: {part2()}")



    