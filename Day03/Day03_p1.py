import re

total = 0
with open("input.txt", "r") as file:

    for line in file:
        line = line.rstrip()
        #line = line.split(" ")
        matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)",line)
        print(matches)
        for match in matches:
            match = match[4:-1].split(',')
            res = int(match[0]) * int(match[1])
            total += res
    

    print(total)
    file.close()

        



    