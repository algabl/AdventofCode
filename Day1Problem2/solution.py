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

similarity_score = 0

for i in range(len(list1)):
    j = 0
    times_in_list_2 = 0
    while list1[i] >= list2[j]:
        j += 1
    
        if list1[i] == list2[j]:
            times_in_list_2 += 1

    similarity_score = similarity_score + (list1[i] * times_in_list_2)

print(similarity_score)


    