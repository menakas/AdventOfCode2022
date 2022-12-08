# https://adventofcode.com/2022/day/4
# Created by: Menaka S. 4 Dec 2022

import sys

cta = 0
ctb = 0
for line in sys.stdin:
    line = line.strip()
    first, second = line.split(',')
    fstart,fend = first.split('-')
    sstart,send = second.split('-')
    if int(fstart) <= int(sstart) and int(fend) >= int(send):
        cta+=1
    elif int(fstart) >= int(sstart) and int(fend) <= int(send):
        cta+=1
    if int(fend) >= int(sstart) and int(fstart) <= int(sstart):
        ctb+=1
    elif int(send) >= int(fstart) and int(sstart) <= int(fstart):
        ctb+=1

print(cta)
print(ctb)
            
