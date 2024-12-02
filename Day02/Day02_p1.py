

total_safe = 0

with open("input.txt", "r") as file:

    for line in file:
        
        line = line.rstrip()
        line = line.split(" ")
        print(list(map(int, line)))
        history = []
        
        if list(map(int, line)) == sorted(list(map(int, line))):
            increasing = True
            #print("Increasing")
        elif list(map(int, line)) == sorted(list(map(int, line)), reverse=True):
            increasing = False
            #print("Decreasing")
        else:
            print("Not in order")
            continue
            
        correct = True

        for i in range(len(line)-1):
            
            if abs( int(line[i]) - int(line[i+1]) ) <= 3 and (not (int(line[i]) == int(line[i+1])) ):
                continue
            else:
                correct = False
                break
        
        if correct:
            print("Safe")
            total_safe += 1
        
    print(total_safe)

                


