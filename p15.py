# https://adventofcode.com/2022/day/15
# Created by: Menaka S. 15 Dec 2022

import sys
from collections import deque

sensors = set()
beacons = set()

stob = dict()
mand = dict()
nobeacons = set()

def getNeighbours(x,y):
    for (i,j) in [(x-1,y), (x,y+1),(x+1,y),(x,y-1)]:
        if (i,j) not in sensors and (i,j) not in beacons:
            yield (i,j)


def manDist(sx,sy,bx,by):
    return abs(sx - bx) + abs(sy-by)


for line in sys.stdin:
    line = line.strip()
    parts = line.split(' ')

    sx= int(parts[2][:-1].split('=')[1])
    sy= int(parts[3][:-1].split('=')[1])
    sensors.add((sx,sy))

    bx= int(parts[8][:-1].split('=')[1])
    by= int(parts[9].split('=')[1])
    beacons.add((bx,by))

    stob[(sx,sy)] = (bx,by)
    mand[(sx,sy)] = manDist(sx,sy,bx,by)

#print(sensors)
#print(beacons)

# Part 1
# row = 10 #for sample input
row = 2000000 # for actual input

for (sx,sy) in stob:
    dist = mand[(sx,sy)]
    rem = dist - abs(sy - row) 
    if sy+dist <= row <= sy or  sy <= row <= sy+dist or sy-dist <= row <= sy:
        for i in range(sx-rem,sx+rem+1):
             if (i,row) not in beacons and (i,row) not in sensors:
                 nobeacons.add((i,row))
   
print(len(nobeacons))


# Part 2
#rows = 20 #for sample input
rows = 4000000 # for actual input
for (sx,sy), dst in mand.items():
    for pt in range( dst + 1 ):
        for tx, ty in [ ( sx - dst - 1 + pt, sy - pt ),
                        ( sx + dst + 1 - pt, sy - pt ),
                        ( sx - dst - 1 + pt, sy + pt ),
                        ( sx + dst + 1 - pt, sy + pt ) ]:
            if ( 0 <= tx <= rows and 0 <= ty <= rows and all( abs( tx - x ) + abs( ty - y ) > d
                      for ((x, y), d) in mand.items() ) ):
                print(tx,ty, tx * 4000000 + ty )
