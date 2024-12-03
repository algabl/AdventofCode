list1 = []
list2 = []
distance = 0

with open("Day1Problem1/input.txt", "r") as file:
    for index, line in enumerate(file):
        line = line.rstrip()
        value1, value2 = line.split("   ")
        list1.append(int(value1))
        list2.append(int(value2))


list1.sort()
list2.sort()

for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])


print(distance)


    