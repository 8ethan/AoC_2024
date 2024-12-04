

total_matches = 0

def checkIfXmas(i,j,lines):

    matches = 0
    diag1 = False
    diag2 = False

    # Check if in bounds
    if i > 0 and j > 0 and i < len(lines)-1 and j < (len(lines[i])-1):

        if (lines[i-1][j-1]=='M' and  lines[i+1][j+1]=='S') or (lines[i-1][j-1]=='S' and  lines[i+1][j+1]=='M'):
            diag1 = True
        if (lines[i+1][j-1]=='M' and  lines[i-1][j+1]=='S') or (lines[i+1][j-1]=='S' and  lines[i-1][j+1]=='M'):
            diag2 = True
        
        if diag1 and diag2:
            matches += 1
            print(f"Match at {i},{j}")

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
            if lines[i][j] == 'A':
                # Find if it makes "X-MAS"
                total_matches += checkIfXmas(i, j, lines)
                #print(total_matches)
    
    print(total_matches)
