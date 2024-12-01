
total = 0

list1 = []
list2 = []

counts = {}

with open("input.txt", "r") as file:

    for line in file:
        
        line = line.rstrip()
        line = line.split("   ")
        
        list1.append(line[0])
        list2.append(line[1])
    
    file.close()

# Generate hashmap of value counts
for i in range(len(list2)):
    if list2[i] not in counts:
        counts[list2[i]] = 1
    else:
        counts[list2[i]] += 1


for i in range(len(list1)):
    if list1[i] not in counts:
        continue
    else:
        total += int(list1[i]) * counts[list1[i]]


print(total)
    