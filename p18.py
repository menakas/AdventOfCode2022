# https://adventofcode.com/2022/day/18
# Created by: Menaka S. 18 Dec 2022

import sys
from collections import deque

cubes = set()
surround = set()

neighbour_delta = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def get_neighbours(cub):
   (x,y,z) = cub
   return [(x+i,y+j,z+k) for (i,j,k) in neighbour_delta]

def parse_input():
    for line in sys.stdin:
        line = line.strip()
        (x,y,z) = map(int,line.split(','))
        cubes.add((x,y,z))

def do_part1():
    total = 0
    for cub in cubes:
        total += sum([0 if i in cubes else 1 for i in get_neighbours(cub)])
    return total
 
def do_part2(): 
    mnx = min(x for (x,y,z) in cubes) -1
    mny = min(y for (x,y,z) in cubes) -1
    mnz = min(z for (x,y,z) in cubes) -1
    mxx = max(x for (x,y,z) in cubes) +1
    mxy = max(y for (x,y,z) in cubes) +1
    mxz = max(z for (x,y,z) in cubes) +1

    queue = deque()
    queue.append((mnx,mny,mnz))
    surround.add((mnx,mny,mnz))

    # Try to build the surrounding area of cubes
    while queue:
        (i,j,k) = queue.popleft()
        for (x,y,z) in get_neighbours((i,j,k)):
            if x > mxx or y > mxy or z > mxz or x < mnx or y < mny or z < mnz:
                continue        
            if (x,y,z) in cubes or (x,y,z) in surround:
                continue
            queue.append((x,y,z))
            surround.add((x,y,z))
      
    # Only those surfaces of a cube that touch this surrounding area are the external sides
    total = 0
    for cub in surround:
        total += sum([1 if i in cubes else 0 for i in get_neighbours(cub)])
    
    return total


parse_input()
print("Part 1:",do_part1())
print("Part 2:",do_part2())

   
