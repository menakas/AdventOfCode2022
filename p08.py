# https://adventofcode.com/2022/day/8
# Created by: Menaka S. 8 Dec 2022

import sys
import pprint

grid = []
for line in sys.stdin:
    line = line.strip()
    grid.append([int(x) for x in line])

#pprint.pprint(grid)


def part1():
    visible = 0
    
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if i ==0 or j == 0 or i == len(grid) - 1 or j == len(grid[i]) - 1:
                visible +=1
            else:
                curr = grid[i][j]
                right = max([x for x in grid[i][j+1:]])
                left = max([x for x in grid[i][:j]])
                below = max([grid[k][j] for k in range(i+1,len(grid))])
                above = max([grid[k][j] for k in range(0,i)])
                if right < curr or left < curr or below < curr or above < curr:
                    visible +=1
    return (visible)


def part2():
    mx = 0
   
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            left = right = above = below = ss = 0
            if not (i ==0 or j == 0 or i == len(grid) - 1 or j == len(grid[i]) - 1):
                right = min([k-j if grid[i][k] >= grid[i][j] else len(grid)-j-1 for k in range(j+1,len(grid))])
                left = min([j-k if grid[i][k] >= grid[i][j] else j for k in range(j-1,-1,-1)])
                below = min([k-i if grid[k][j] >= grid[i][j] else len(grid)-i-1 for k in range(i+1,len(grid))])
                above = min([i-k if grid[k][j] >= grid[i][j] else i for k in range(i-1,-1,-1)])
                ss = right * left * above * below
                if ss > mx:
                   mx = ss

    return (mx)

print(part1())
print(part2())
 
