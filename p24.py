# https://adventofcode.com/2022/day/24
# Created by: Menaka S. 24 Dec 2022

import sys

def parse_input():
    for line in sys.stdin:
         line = line.strip()
         grid.append(list(line))
   
def move_bliz(bliz):
    global mx,my
    (x, y, sym) = bliz
    match sym:
        case ">":
            return (x, 1, sym) if y + 1 > my-2 else (x, y + 1, sym)
        case "<":
            return (x, my-2, sym) if y - 1 < 1 else (x, y - 1, sym)
        case "^":
            return (mx-2, y, sym) if x - 1 < 1 else (x - 1, y, sym)
        case "v":
            return (1, y, sym) if x + 1 > mx-2 else (x + 1, y, sym)

def find_min_path(cx,cy,sx,sy,ex,ey,mins):
    global mn, seen,bliz_ss,wait

    seen.add((cx,cy,mins))

    if cx == ex and cy == ey:
        mn = min(mn,mins)
        return

    if mins >= mn:
        return

    neighbours = [(cx + i, cy + j) for (i, j) in [(0, 1), (1, 0), (-1, 0), (0, -1), (0, 0)]]

    for (x,y) in neighbours:
        #print(cx,cy, "=>", x,y)
        if ((x,y, mins + 1) in seen or (x,y) in bliz_ss[mins]):
            continue
        if not (1 <= x <= mx-2 and 1 <= y <= my-2) and not (x,y) == (sx,sy) and not (x,y) == (ex,ey):
            continue
        find_min_path(x,y,sx,sy,ex,ey,mins + 1)

grid = []
blizs = []
bliz_ss = {}

parse_input()

mx = len(grid)
my = len(grid[0])

for i in range(mx):
    for j in range(my):
        if grid[i][j] in "<>^v":
            blizs.append((i, j, grid[i][j])) 

#Calc blizzard positions for several mins
for i in range(2000):
    blizs = [move_bliz(b) for b in blizs]
    bliz_ss[i] = set([(x, y) for (x, y, _) in blizs])

for j in range(len(grid[0])):
     if grid[0][j] == '.':
          sx,sy = 0,j
     if grid[len(grid)-1][j] == '.':
          ex,ey = len(grid)-1,j

seen = set()
mn = 1000
find_min_path(sx,sy,sx,sy,ex,ey,0)
lastmn = mn

print("Part 1:",mn)

seen = set()
mn = 1000
find_min_path(ex,ey,ex,ey,sx,sy,lastmn)
lastmn = mn

print("Part 2.1:",mn)

seen = set()
mn = 1000
find_min_path(sx,sy,sx,sy,ex,ey,lastmn)
print("Part 2.2:",mn)

