
# https://adventofcode.com/2022/day/3
# Created by: Menaka S. 3 Dec 2022

import sys

def parta(common):
    n = len(line)//2
    common = set(line[:n]).intersection(set(line[n:]))
    return calc_priority(common)

def partb(common):
    return calc_priority(common)

def calc_priority(common):
    sum = 0
    for item in common:
        if item.islower():
            sum += ord(item) - ord('a') + 1
        if item.isupper():
            sum += ord(item) - ord('A') + 27
    return sum

prioritiesa =0
prioritiesb =0
ct = 0
for line in sys.stdin:
    line = list(line.strip())
    prioritiesa += parta(line)
    if not ct:
        common = set(line)
    else:
        common = common.intersection(set(line))
    ct+=1
    if ct == 3:
       ct = 0
       prioritiesb += partb(common)

print(prioritiesa)
print(prioritiesb)
            
