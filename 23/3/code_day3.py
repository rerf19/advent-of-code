#Global
lines = []

def getLines():
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            lines.append(line.strip())
        

def getPositions(inicial_line,inicial_j):
    number = ''
    for i in range(inicial_line,len(lines)):
        if not i == inicial_line: inicial_j = 0
        skip = False
        for j in range(inicial_j+1,len(lines[i])):
            if skip:
                if not lines[i][j].isdigit():
                    return i,pos1,pos2,number
                else:
                    pos2 = j
                    number = number + lines[i][j]
                    if j == len(lines[i])-1:
                        return i,pos1,pos2, number
            else:
                if lines[i][j].isdigit():
                    pos1 = j
                    pos2 = j
                    number = lines[i][j]
                    skip = True

def checkNeighbours(l, pos1, pos2):
    n1 = 1
    n2 = 2
    if l == 0: n1 = 0
    if l == (len(lines) - 2): n2 = 1
    if l == (len(lines) - 1): n2 = 0
    t1 = 1
    t2 = 2
    if pos1 == 0: t1 = 0
    for i in range(l-n1,l+n2):
        if pos2 == len(lines[i]) - 1: t2 = 1
        for j in range(pos1-t1,pos2+t2):
            if not lines[i][j].isdigit():
                if lines[i][j] != '.':
                    print(l,number,lines[i][j])
                    #print('found')
                    return True
                
    return False

getLines()

line = 0
p1 = 0
p2 = 0
add = 0

while line <= (len(lines) - 1) :
        
        line,p1,p2, number = getPositions(line,p2)
        valid = checkNeighbours(line,p1,p2)
        if valid:
            add = add + int(number)
            #print(add)

        if p2 == 139:
            line += 1
            p2 = 0
        
        #print("Line: " + str(line))
        #print("Number: " + str(number))


#print(len(lines))
print(add)


