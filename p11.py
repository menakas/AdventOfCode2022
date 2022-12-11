# https://adventofcode.com/2022/day/11
# Created by: Menaka S. 11 Dec 2022

import sys
from copy import deepcopy

monkeyItems = []
monkeyOps = []
monkeyVal = []
monkeyTest = []
monkeyTrue = []
monkeyFalse = []

for line in sys.stdin:
    line = line.strip().strip(':')
    parts = line.split(' ')
    if len(parts) == 1:
       continue
    if parts[0] == 'Starting':
       monkeyItems.append([int(x) for x in line.split(':')[1].split(', ')])
    if parts[0]== 'Operation:':
       if parts[4] == '*' and parts[5] == 'old':
           monkeyOps.append('**')
           monkeyVal.append(2)
       else:
           monkeyOps.append(parts[4])
           monkeyVal.append(int(parts[5]))
    if parts[0] == 'Test:':
       monkeyTest.append(int(parts[3]))
    if parts[1] == 'true:':
       monkeyTrue.append(int(parts[5]))
    if parts[1] == 'false:':
       monkeyFalse.append(int(parts[5]))

print(monkeyItems)
print(monkeyOps)
print(monkeyVal)
print(monkeyTest)
print(monkeyTrue)
print(monkeyFalse)

def doPart(part):
    # Part 2
    lcm  = 1
    if part == 2:
        for x in monkeyTest:
            lcm *= x
    
    rond = 0
    if part == 1:
        totalronds = 20
    else:
        totalronds = 10000

    monkeyWorries = deepcopy(monkeyItems)
    times = [0 for x in range(0,len(monkeyItems))]
    
    while rond <totalronds:
        for i in range(0,len(monkeyWorries)):
            for j in range(0,len(monkeyWorries[i])):
                times[i] +=1
                if monkeyOps[i] == '*':
                    monkeyWorries[i][j] *= monkeyVal[i]
                if monkeyOps[i] == '+':
                    monkeyWorries[i][j] += monkeyVal[i]
                if monkeyOps[i] == '**':
                    monkeyWorries[i][j] **= monkeyVal[i]
                if part == 1:
                    monkeyWorries[i][j] //=3 
                if monkeyWorries[i][j]%monkeyTest[i] :
                   # false
                   monkeyWorries[monkeyFalse[i]].append(monkeyWorries[i][j])
                else:
                   #true
                   if part == 2:
                      monkeyWorries[i][j] %= lcm
                   monkeyWorries[monkeyTrue[i]].append(monkeyWorries[i][j])
            monkeyWorries[i] = []
        #print("After rond,",rond,"times ",times,monkeyWorries)
        rond +=1

    times.sort()
    print(times)
    return(times[-2]*times[-1])
    
    
print(doPart(1))
print(doPart(2))
