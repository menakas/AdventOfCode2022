# https://adventofcode.com/2022/day/17
# Created by: Menaka S. 17 Dec 2022

import sys

grid = set()

seen = dict()
hts = dict()

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
  
def calc_height(rocks,ht,oldrocks,oldht,mxrocks):
    global hts

    mxrocks -= oldrocks
    deltarocks = rocks - oldrocks
    deltaht = ht - oldht
    q = mxrocks//deltarocks
    r = mxrocks%deltarocks
    return (q* deltaht + hts[oldrocks+r]) + 1

def signature(ht):
    sign = []
    for x in range(7):
        for y in range(ht-30,ht):
            if (x,y) in grid:
                sign.append((x,ht-y))
    return str(sign)
  
def do_part(lst):
    global htoffset,offset,multiple

    rocks = 0
    mxheight = -1
    cshape = 0
    cjet = -1

    rock=start_rock(cshape,mxheight)
    while True:
        cjet = get_next_index(lst,cjet)        
        rock = fall_rock(push_rock(rock,lst[cjet]),mxheight)
        if not len(rock):
           rocks += 1
           ht = get_max_height()

           sign = (cshape, cjet, signature(ht))
           if sign in seen: # and ht >2022:
               oldht,oldrocks = seen[sign]
               return(
                calc_height(rocks,ht,oldrocks,oldht,2022),
                calc_height(rocks,ht,oldrocks,oldht,1000000000000)
              )

           if sign not in seen:
               seen[sign] = (ht,rocks)
               hts[rocks] = ht

           cshape = get_next_index(shapes,cshape)
           mxheight = get_max_height()
           rock=start_rock(cshape,mxheight)
  
lst = parse_input()
part1,part2 = do_part(lst)
print("Part 1:",part1)
print("Part 2:",part2)
