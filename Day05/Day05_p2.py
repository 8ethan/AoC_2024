

def swap_values(idx1, idx2, pages):
    temp = pages[idx1]
    pages[idx1] = pages[idx2]
    pages[idx2] = temp


def check_correct(page_list):

    previous = [page_list[0]]

    for i in range(len(page_list)-1):         
            
            # Check previous against dict
            for j in range(len(previous)):
                if previous[j] not in prev_dict:
                    continue
                if page_list[i+1] in prev_dict[previous[j]]:
                    #print(f"page {page_list[i+1]} cannot have predecessor {previous[j]}")
                    return (i+1, j)
            
            previous.append(page_list[i+1])
    
    #print("Correct order")
    return (-1, -1)
    

with open("input.txt", "r") as file:
    
    mid_count = 0
    prev_dict = {}

    for line in file:
        line = line.rstrip()
        if line == "":
            break

        line = line.split("|")
        if line[1] not in prev_dict:
            prev_dict[line[1]] = [line[0]]
        else:
            prev_dict[line[1]].append(line[0])
    
    print("dict constructed")
    #print(prev_dict)

    for line in file:
        line = line.rstrip()
        line = line.split(",")   
        print(line)

        correct = check_correct(line)
        
        if correct[0] != -1:
            while correct[0] != -1:
                #print("Attempting re-order")
                swap_values(correct[0], correct[1], line)
                correct = check_correct(line)
                
            
            print(line)
            mid_count += int(line[(len(line)//2)])
            print("-----------------------")
        else:
            print("Correct Initial Line - Ignored")


    print(mid_count)

            