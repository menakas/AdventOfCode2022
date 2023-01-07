# https://adventofcode.com/2022/day/23
# Created by: Menaka S. 23 Dec 2022

import sys

grid = dict()

neighbour_delta = [[(-1,0), (-1,-1),(-1,1)],
                   [(1,0), (1,-1),(1,1)],
                   [(0,-1), (1,-1),(-1,-1)],
                   [(0,1),(-1,1),(1,1)]]

eight_neighbours = [(1,0), (1,-1),(1,1), (0,-1), (0,1),(-1,-1), (-1,0),(-1,1)]

def draw_grid(rond,mn,mx):
   print("Round ", rond)
   for i in range(mn,mx):
      print(i,end=' ')
      for j in range(mn,mx):
          if (i,j) not in grid:
               print('.',end=' ')
          else:
               print(grid[(i,j)],end=' ')
      print("\n")
   print("===\n")

def parse_input():
    i = 0
    for line in sys.stdin:
         line = line.strip()
         parts = list(line)
         for j in range(len(parts)):
             grid[(i,j)] = parts[j]
         i+=1
   
def propose_move(x,y):
    for (i,j) in eight_neighbours:
         if (x+i,y+j) in grid and grid[(x+i,y+j)] == '#':
             break
    else:
        return (x,y)
    
    for dlst in neighbour_delta:
        for (i,j) in dlst:
            if (x+i,y+j) in grid and grid[(x+i,y+j)] == '#':
                break
        else:
            return (x+dlst[0][0],y+dlst[0][1])
    return(x,y)
 

def do_part():
    rond = 0

    while True:
        propose = dict()
        inv_propose = dict()
        for k,v in grid.items():
             if v == '#':
                 (x,y) = k
                 k = propose_move(x,y)
                 if k != (x,y):
                     propose[(x,y)] = k

        if not len(propose.items()):
            print("Part 2:", rond+1)
            return

        for k,v in propose.items():
            if v in inv_propose:
               inv_propose[v].append(k)
            else:
               inv_propose[v] = [k]

        for k,v in inv_propose.items():
            if v is not None and len(v) == 1: 
                grid[v[0]] = '.'
                grid[k] = '#'

        rond +=1
        #draw_grid(rond,-3,40)
        neighbour_delta.append(neighbour_delta.pop(0))
        if rond == 10:
            minx = min([i for ((i,j),y) in grid.items() if grid[(i,j)] == '#'])
            maxx = max([i for ((i,j),y) in grid.items() if grid[(i,j)] == '#'])
            miny = min([j for ((i,j),y) in grid.items() if grid[(i,j)] == '#'])
            maxy = max([j for ((i,j),y) in grid.items() if grid[(i,j)] == '#'])
            
            empty = 0
            for i in range(minx,maxx+1):
                for j in range(miny,maxy+1):
                    if (i,j) not in grid or grid[(i,j)] != '#':
                        empty +=1
            print("Part 1:", empty)

parse_input()
#draw_grid(0,-3,20)
do_part()
