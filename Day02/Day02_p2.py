

total_safe = 0

with open("input.txt", "r") as file:

    for line in file:
        
        line = line.rstrip()
        line = line.split(" ")
        line = list(map(int, line))
        print(line)

        is_safe = True
        
        # Brute force because idk what I am doing
        for i in range(len(line)):
            temp = line.copy()
            del temp[i]
            print(temp)

            n_pos = 0
            n_neg = 0
            is_safe = True

            for j in range(len(temp)-1):
                
                diff = temp[j] - temp[j+1]

                if diff > 0:
                    if n_neg > 0 or diff > 3:
                        is_safe = False
                        break
                    n_pos += 1
                elif diff < 0:
                    if n_pos > 0 or diff < -3:
                        is_safe = False
                        break
                    n_neg += 1
                else:
                    is_safe = False
                    break
            
            if is_safe:
                print("Subset is safe")
                break
            else:
                print("Subset unsafe")

            
        if is_safe:
            print("Safe")
            total_safe += 1
        else:
            print("UNSAFE --------------------------------------------------------------------------")

        print("")

    print(total_safe)
