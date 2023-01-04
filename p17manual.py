# https://adventofcode.com/2022/day/17
# Created by: Menaka S. 17 Dec 2022

import sys

grid = set()

pattern = []
htoffset = 0
offset = 359 #30 for sample
multiple = 1715 #35 for sample
#pattern = '02340121201212013200133401230113220'

shapes = [ 
              [(2,0),(3,0),(4,0),(5,0)],       # -
              [(3,0),(2,1),(3,1),(4,1),(3,2)], # +
              [(2,0),(3,0),(4,0),(4,1),(4,2)], # _|
              [(2,0),(2,1),(2,2),(2,3)],       # |
              [(2,0),(3,0),(2,1),(3,1)]        # |
            ]

def add_tup(tup1,tup2):
   return tuple(map(lambda i, j: i + j, tup1, tup2)) 
    
def fall_rock(rock,mxheight):
     if any([add_tup((x,y),(0,-1)) in grid or not y for (x,y) in rock]) :
         for i in rock:
            grid.add(i)
         return []
     else:
         return [add_tup(i,(0,-1)) for i in rock]

def get_next_index(lst,ind):
    return ind+1 if ind < len(lst)-1 else 0

def get_max_height():
    return max([k[1] for k in grid]) if len(grid) > 0 else 0
 
def parse_input():
    return list(sys.stdin.read().strip())

def push_rock(rock,push):
   if push == '>':
      if max([x for (x,y) in rock]) == 6: #right wall
         return rock
      elif any([add_tup((x,y),(1,0)) in grid for (x,y) in rock]):
         return rock
      else:
         return [add_tup(i,(1,0)) for i in rock]
   if push == '<':
      if min([x for (x,y) in rock]) == 0: #left wall
         return rock
      elif any([add_tup((x,y),(-1,0)) in grid for (x,y) in rock]):
         return rock
      else:
         return [add_tup(i,(-1,0)) for i in rock]
   
def start_rock(ind,mxheight):
   return [(add_tup(item,(0,mxheight+4))) for item in shapes[ind]]
  
def do_part1(lst):
    global htoffset,offset,multiple
    rocks = 0
    mxheight = -1
    cshape = 0
    cjet = -1

    #lt = -1 #for finding pattern in Part 2 

    rock=start_rock(cshape,mxheight)
    while True:
        cjet = get_next_index(lst,cjet)        
        rock = fall_rock(push_rock(rock,lst[cjet]),mxheight)
        if not len(rock):
           rocks += 1
           ht = get_max_height()

           # Part 1 
           if rocks == 2022:
               ht2022 = ht

           # Part 2
           # for finding pattern in Part 2
           #print(ht,lt,ht-lt)
           #lt = ht

           if rocks == offset:
               htoffset = ht
           if offset < rocks <=(multiple+offset):
              pattern.append(ht-htoffset)

           if rocks >= offset+ multiple:
               break

           cshape = get_next_index(shapes,cshape)
           mxheight = get_max_height()
           rock=start_rock(cshape,mxheight)

    return ht2022+1
  
#Method 1 manual
def do_part2(): 
    rocks = 1000000000000
    rocks -= offset

    qrocks = rocks//multiple
    rrocks = rocks%multiple 

    return (htoffset + (qrocks * pattern[-1]) + pattern[rrocks])


lst = parse_input()
print("Part 1:",do_part1(lst))
print("Part 2:",do_part2())
