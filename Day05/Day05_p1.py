


with open("test.txt", "r") as file:
    
    mid_count = 0
    hash_table = {}

    for line in file:
        line = line.rstrip()
        if line == "":
            break

        line = line.split("|")
        if line[1] not in hash_table:
            hash_table[line[1]] = [line[0]]
        else:
            hash_table[line[1]].append(line[0])
    
    print("dict constructed")
    print(hash_table)

    for line in file:
        line = line.rstrip()
        line = line.split(",")   
        print(line)

        previous = [line[0]]
        correct = True

        for i in range(len(line)-1):
            
            # Check previous against dict
            for j in range(len(previous)):
                if previous[j] not in hash_table:
                    continue
                if line[i+1] in hash_table[previous[j]]:
                    print(f"page {line[i+1]} cannot have predecessor {previous[j]}")
                    correct = False
                    break
            if not correct:
                break
            previous.append(line[i+1])
        if correct:
            mid_count += int(line[(len(line)//2)])
    
    print(mid_count)

            






