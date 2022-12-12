import sys
from collections import deque

grid = []

for line in sys.stdin:
    line = line.strip()
    grid.append([x for x in line])

#print(grid)

rows = len(grid)
cols = len(grid[0])
toProcess = deque()

def getCoords(char):
    for i in range(0,rows):
        for j in range(0,cols):
            if grid[i][j] == char:
                return(i,j)

def getneighbours(x,y):
    for (i,j) in [(x-1,y), (x,y+1),(x+1,y),(x,y-1)]:
        if 0<=i<len(grid) and 0<=j<len(grid[i]) and ord(grid[i][j]) - ord(grid[x][y]) <= 1:
            yield (i,j)


start= getCoords('S')
endpoint= getCoords('E')
grid[start[0]][start[1]] = 'a'
grid[endpoint[0]][endpoint[1]] = 'z'

#print(start,endpoint)

heights = [[ord(grid[i][j]) - ord('a')+1 for j in range(0,cols)] for i in range(0,rows)]
#print(heights)


def getShortestPath():
    global toProcess
    visited = set()
    while toProcess:
        #print(toProcess)
        (x,y),steps = toProcess.popleft()
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if (x,y) == endpoint:
            return(steps)
        for nx,ny in getneighbours(x,y):
            #print("For", x, y,"Adding",nx,ny)
            if ((nx,ny),steps+1) not in toProcess:
                toProcess.append(((nx,ny),steps+1)) #Adding all coords that take 'steps+1' steps to reach from Start

   
 
# Part 1
toProcess.append((start,0))
print(getShortestPath())

# Part 2
toProcess = deque()
for i in range(0,rows):
    for j in range(0,cols):
        if grid[i][j] == 'a':
            toProcess.append(((i,j),0))
print(getShortestPath())
