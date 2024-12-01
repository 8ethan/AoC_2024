
list1 = []
list2 = []

with open("input.txt", "r") as file:

    for line in file:
        
        line = line.rstrip()
        line = line.split("   ")
        
        list1.append(line[0])
        list2.append(line[1])
    
    file.close()
    

list1 = sorted(list1)
list2 = sorted(list2)

diff = 0
for i in range(len(list1)):

    diff += abs(int(list1[i]) - int(list2[i]))


print(diff)
    