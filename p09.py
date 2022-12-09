# https://adventofcode.com/2022/day/9
# Created by: Menaka S. 9 Dec 2022

import sys

grid = []
hcurr = (0,0)

# Part 1 Initialization
positions1 = set()
tcurr = (0,0)

# Part 2 Initialization
positions2 = set()
tails = []
for i in range(0,9):
    tails.append((0,0))

def get_next(dir,tup):
    if dir == 'L':
        return (tup[0]-1,tup[1])
    if dir == 'R':
        return (tup[0]+1,tup[1])
    if dir == 'U':
        return (tup[0],tup[1]-1)
    if dir == 'D':
        return (tup[0],tup[1]+1)

def get_tail(hd,tl):
   if abs(hd[0] - tl[0]) <= 1 and abs(hd[1] - tl[1]) <= 1:
      return tl
   elif abs(hd[0] - tl[0]) == 2 and abs(hd[1] - tl[1]) == 2: #Required for Part 2
      return ((hd[0]+tl[0])//2,(hd[1]+tl[1])//2)
   elif abs(hd[0] - tl[0]) == 2:
      return ((hd[0]+tl[0])//2,hd[1])
   elif abs(hd[1] - tl[1]) == 2:
      return (hd[0],(hd[1]+tl[1])//2)
   else:
      print("Something wrong: head ",hd[0], hd[1], "tail ", tl, tl[0],tl[1])
      exit()
      
      
for line in sys.stdin:
    line = line.strip()
    (dir,dist) = line.split(' ')
    dist = int(dist)
    while(dist):
        hcurr=get_next(dir,hcurr)
        dist -=1

        #Part 1
        tcurr = get_tail(hcurr,tcurr)
        positions1.add(tcurr)
          
        #Part 2
        tails[0] = get_tail(hcurr,tails[0])
        for i in range(1,9):
            tails[i] = get_tail(tails[i-1],tails[i])
        positions2.add(tails[8])
        
       
#Part 1
print(len(positions1))

#Part 2
print(len(positions2))
