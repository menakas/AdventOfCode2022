# https://adventofcode.com/2022/day/10
# Created by: Menaka S. 10 Dec 2022

import sys

cycle = 1
X = 1
lastX = 1
total = 0
here = 0

grid = ['.' for i in range(0,240)]


def drawGrid():
    for i in range(0,6):
       line = ''.join(grid[i*40: (i*40)+40])
       print(line) 

def drawPos(cycle,X):
    if cycle%40 in (X-1,X,X+1):
        grid[cycle] = '#'

drawPos(0,X)
drawPos(1,X)

for line in sys.stdin:
    line = line.strip()
    if line == 'noop':
        cycle +=1

        drawPos(cycle,X)
    else: # addx
        (_, vl) = line.split(' ')
        lastX = X
        X += int(vl)
        cycle +=2

        drawPos(cycle-1,X)
        drawPos(cycle,X)

    if cycle%40 == 20:
       total += (cycle * X)
       here += 40
    elif cycle > here and cycle%40 == 21:
       total += ((cycle-1) * lastX)
       

print(total)
drawGrid()
     
