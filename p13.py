# https://adventofcode.com/2022/day/13
# Created by: Menaka S. 13 Dec 2022

import sys
import functools
import ast

lpairs = []
rpairs = []

left = 1
for line in sys.stdin:
    line = line.strip()
    if line:
        if left: 
            lpairs.append(ast.literal_eval(line))
            left = 0
        else:
            rpairs.append(ast.literal_eval(line))
            left = 1

def comparelist(x,y):
    #print("Comparing lists ", x , " and ", y)
    if not len(y) and len(x):
       return -1
    elif not len(x) and len(y):
       return 1
    for (i,j) in zip(x,y):
        vlue = compare(i,j)
        if vlue:
           return vlue
    if len(x) > len(y):
        return -1
    elif len(x) < len(y):
        return 1
    else:
        return 0

def compare(x,y):
    #print("Comparing", x, " and ", y)
    if type(x) == int and type(y) == int:
         if x < y:
            return 1
         if x > y:
            return -1
         else:
            return 0
    if type(x) == list and type(y) == list:
         return comparelist(x,y)
    if type(x) == int and type(y) == list:
         return comparelist([x],y)
    if type(x) == list and type(y) == int:
         return comparelist(x,[y])

total= sum([max(0,comparelist(lpairs[i],rpairs[i])) * (i+1) for i in range(len(lpairs))])

print(total)

# Part 2
everything = lpairs + rpairs + [[[2]], [[6]]]
everything.sort(key=functools.cmp_to_key(comparelist),reverse=True)
print(( everything.index([[2]]) + 1 ) * ( everything.index([[6]]) + 1 ))
