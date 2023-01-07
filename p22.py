# https://adventofcode.com/2022/day/22
# Created by: Menaka S. 22 Dec 2022

import sys
import re

grid = []
minrows = []
maxrows = []
mincols = []
maxcols = []
griddict = dict()
isgrid = 1
instr = []

# Hardcoded for my input - Doesn't work for sample input Part 2
def mappoint(x,y,f):
   if f == 0:
       if 0 <= x < 50:
          return (149-x,99,2) 
       if 50 <= x < 100:
          return (49,x+50,3) 
       if 100 <= x < 150:
          return (149-x,149,2) 
       if 150 <= x < 200:
          return (149,x-100,3)
   if f == 1:
       if 0 <= y < 50:
          return (0,y+100,1) 
       if 50 <= y < 100:
          return (y+100,49,2) 
       if 100 <= y < 150:
          return (y-50,99,2) 
   if f == 2:
       if 0 <= x < 50:
          return (149-x,0,0) 
       if 50 <= x < 100:
          return (100,x-50,1) 
       if 100 <= x < 150:
          return (149-x,50,0) 
       if 150 <= x < 200:
          return (0,x-100,1)
   if f == 3:
       if 0 <= y < 50:
          return (50+y,50,0) 
       if 50 <= y < 100:
          return (y+100,0,0) 
       if 100 <= y < 150:
          return (199,y-100,3) 

def parse_input():
    global isgrid,instr
    for line in sys.stdin:
         line = line.strip('\n')
         if not line:
            isgrid -=1
         if isgrid:
             grid.append(list(line))
         else:
             instr = re.findall('\d+[RL]?',line)

def turn(face,cdir):
    if cdir == 'R':
       return face +1 if face<3 else 0
    else:
       return face -1 if face>0 else 3

 
def move(x,y,f,part):
    global griddict,minrows,maxrows,mincols,maxcols
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    if (x+delta[f][0],y+delta[f][1]) in griddict:
      if griddict[(x+delta[f][0],y+delta[f][1])] != '#':
          #print("...",x,y,f, x+delta[f][0], y+delta[f][1],f)
          return (x+delta[f][0],y+delta[f][1],f)
      else:
          return (x,y,f)
    if part == 2:
        (nx,ny,nf) = mappoint(x,y,f)
        if (nx,ny) in griddict and griddict[(nx,ny)] != '#':
            return (nx,ny,nf)
        else:
          return (x,y,f)
    if f == 0 and griddict[(x,minrows[x])] != '#':
           return (x,minrows[x],f)
    elif f == 1 and griddict[(mincols[y],y)] != '#':
           return (mincols[y],y,f)
    elif f == 2 and griddict[(x,maxrows[x])] != '#':
           return (x,maxrows[x],f)
    elif f == 3 and griddict[(maxcols[y],y)] != '#':
           return (maxcols[y],y,f)
    else:
      return (x,y,f)


def do_part(part):
    global grid,instr 
    
    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
             if grid[i][j] != ' ':
                 griddict[(i,j)] = grid[i][j]
        
    lens = [] 
    for i in range(0,len(grid)):
        minrows.append(min(y for(x,y) in griddict if x == i))
        maxrows.append(max(y for(x,y) in griddict if x == i))
        lens.append(len(grid[i]))
    for i in range(0,max(lens)):
        mincols.append(min(x for(x,y) in griddict if y == i))
        maxcols.append(max(x for(x,y) in griddict if y == i))

    currx = min( x for (x,y) in griddict)
    curry = min( y for (x,y) in griddict if x == currx)
    currface = 0 #Right
    for i in range(len(instr)):
        cins = instr[i]
        if cins[-1] in 'RL':
           cdir = cins[-1]
           cins = cins[:-1]
        csteps = int(cins)
        while csteps:
            currx,curry,currface = move(currx,curry,currface,part)  
            csteps -=1
        if i < len(instr)-1:
            currface = turn(currface, cdir)

    #print(currx,curry,currface)
    currx +=1
    curry +=1
    return (currx * 1000) + ( curry * 4) + currface

parse_input()
print(do_part(1))
print(do_part(2))
