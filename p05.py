# https://adventofcode.com/2022/day/5
# Created by: Menaka S. 5 Dec 2022

import sys

rowsa = []
rowsb = []
first = 1
for line in sys.stdin:
    if '[' in line:
        n =  4
        if first:
           rowsa = [[line[i:i+n].strip().lstrip('[').rstrip(']')] for i in range(0, len(line), n)]
           first = 0
        else:
           tlist = [line[i:i+n].strip().lstrip('[').rstrip(']') for i in range(0, len(line), n)]
           for j in range(0,len(tlist)):
               rowsa[j].append(tlist[j])
               rowsa[j] = list(filter(('').__ne__, rowsa[j]))
    elif 'move' in line:
       line = line.strip()
       parts = line.split(' ')
       num = int(parts[1])
       fr = int(parts[3])-1
       to = int(parts[5])-1
       # Part 1
       for a in range(0,num):
           rowsa[to].insert(0,rowsa[fr][a])
       rowsa[fr] = rowsa[fr][num:]
       # Part 2
       rowsb[to] = rowsb[fr][:num] + rowsb[to]
       rowsb[fr] = rowsb[fr][num:]
    else:
       rowsb = rowsa.copy()

txta = ''
txtb = ''
for i in range(0,len(rowsa)):
   txta += rowsa[i][0]
   txtb += rowsb[i][0]
print(txta,txtb)
      
        
        
