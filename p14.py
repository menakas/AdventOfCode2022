# https://adventofcode.com/2022/day/14
# Created by: Menaka S. 14 Dec 2022

import sys

grid = set()

def drawPath(x1,y1, x2,y2,char):
    if x1 == x2:
       if y1 > y2:
           step = -1
       else:
           step = 1
       for i in range(y1,y2+step,step):
           grid.add((x1,i))
    elif y1 == y2:
       if x1 > x2:
           step = -1
       else:
           step = 1
       for i in range(x1,x2+step,step):
           grid.add((i,y1))

def doPart(part):
    x, y = (500, 0)   
    blocked = False
    while not blocked:
        nx, ny = x, y
        while True:
            if part == 1 and not any(i == nx and j >= ny for i,j in grid):
                blocked = True
                break
            if (part == 2 and ny+1 < mx) or part == 1:
                if (nx, ny+1) not in grid:
                    ny += 1;
                    continue
                if (nx-1, ny+1) not in grid:
                    nx -= 1;
                    ny += 1;
                    continue
                if (nx+1, ny+1) not in grid:
                    nx += 1;
                    ny += 1;
                    continue
            if part == 2 and ny == y:
                blocked = True
                break
            grid.add((nx, ny))
            grido.add((nx, ny))
            break
    print(len(grido))

for line in sys.stdin:
    line = line.strip()
    if line:
       posns = line.split(' -> ')
    first = posns[0].split(',')
    for i in range(1,len(posns)):
       (x,y) = posns[i].split(',')
       nxt = posns[i].split(',')
       drawPath(int(first[0]),int(first[1]),int(nxt[0]),int(nxt[1]),'#')
       first = nxt

gridorig = grid.copy()
grido = set()
doPart(1)

mx = max([y for (x,y) in grid]) + 2
grid = gridorig.copy()
grido = set()
grido.add((500,0))
doPart(2)
