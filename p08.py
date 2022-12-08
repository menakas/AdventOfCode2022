# https://adventofcode.com/2022/day/8
# Created by: Menaka S. 8 Dec 2022

import sys
import pprint

grid = []
for line in sys.stdin:
    grid.append([int(x) for x in line.strip()])

#pprint.pprint(grid)

bounds = [0,len(grid)-1]

def part1():
    visible = 0
    
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            visible += i in bounds or j in bounds or min(
                        max([x for x in grid[i][j+1:]]),
                        max([x for x in grid[i][:j]]),
                        max([grid[k][j] for k in range(i+1,len(grid))]),
                        max([grid[k][j] for k in range(0,i)])
                    ) < grid[i][j]
    return (visible)

def part2():
    mx = 0
   
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if i not in bounds and j not in bounds:
                mx = max(mx,
                        min([k-j if grid[i][k] >= grid[i][j] else len(grid)-j-1 for k in range(j+1,len(grid))]) *
                        min([j-k if grid[i][k] >= grid[i][j] else j for k in range(j-1,-1,-1)]) *
                        min([k-i if grid[k][j] >= grid[i][j] else len(grid)-i-1 for k in range(i+1,len(grid))]) *
                        min([i-k if grid[k][j] >= grid[i][j] else i for k in range(i-1,-1,-1)])
                   )
    return (mx)

print(part1())
print(part2())
 
