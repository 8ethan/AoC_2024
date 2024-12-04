

total_matches = 0

def checkIfXmas(i,j,lines):

    matches = 0

    #Left
    if j >= 3:
        if lines[i][j-1]+lines[i][j-2]+lines[i][j-3] == "MAS":
            matches += 1
            print(f"Found left match at {i},{j}")
    
    #Right
    if j <= (len(lines[i])-4):
        if lines[i][j+1]+lines[i][j+2]+lines[i][j+3] == "MAS":
            matches += 1
            print(f"Found right match at {i},{j}")

    # Upwards
    if i >= 3:
        #Straight up
        if lines[i-1][j]+lines[i-2][j]+lines[i-3][j] == "MAS":
            matches += 1
            print(f"Found up match at {i},{j}")

        # Up Left Diagonal
        if j >= 3:
            if lines[i-1][j-1]+lines[i-2][j-2]+lines[i-3][j-3] == "MAS":
                matches += 1
                print(f"Found up-left match at {i},{j}")
        
        # Up Right Diagonal
        if j <= (len(lines[i])-4):
            if lines[i-1][j+1]+lines[i-2][j+2]+lines[i-3][j+3] == "MAS":
                matches += 1
                print(f"Found up-right match at {i},{j}")
    
    # Downwards
    if i <= (len(lines)-4):
        # Straight down
        if lines[i+1][j]+lines[i+2][j]+lines[i+3][j] == "MAS":
            matches += 1
            print(f"Found down match at {i},{j}")

        # Down Left Diagonal
        if j >= 3:
            if lines[i+1][j-1]+lines[i+2][j-2]+lines[i+3][j-3] == "MAS":
                matches += 1
                print(f"Found down-left match at {i},{j}")
        
        # Up Right Diagonal
        if j <= (len(lines[i])-4):
            if lines[i+1][j+1]+lines[i+2][j+2]+lines[i+3][j+3] == "MAS":
                matches += 1
                print(f"Found down-right match at {i},{j}")

    
    return matches

with open("input.txt", "r") as file:
    
    lines = []

    for line in file:
        line = line.rstrip()
        lines.append(line)
        #print(line)
    

    for i in range(len(lines)):

        for j in range(len(lines[i])):
            #print(lines[i])
            if lines[i][j] == 'X':
                # Find if it makes XMAS
                total_matches += checkIfXmas(i, j, lines)
                print(total_matches)
