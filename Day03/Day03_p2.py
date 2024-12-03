import re

total = 0
with open("input.txt", "r") as file:
    
    enabled = True

    for line in file:
        line = line.rstrip()
        #line = line.split(" ")
        matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)",line)
        
        print(matches)
        for match in matches:
            print(match)
            if  match.startswith("do()"):
                enabled = True
                print("Enabled")
                continue
            elif match.startswith("don't()"):
                enabled = False
                print("Disabled")
                continue

            if enabled:
                match = match[4:-1].split(',')
                res = int(match[0]) * int(match[1])
                print(res)
                total += res
    
    print("")
    print(total)
    file.close()