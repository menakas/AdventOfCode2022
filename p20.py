# https://adventofcode.com/2022/day/20
# Created by: Menaka S. 20 Dec 2022

import sys

allnodes = []
head = None
curr = None

class Node:
 
    # Constructor to create a new node
    def __init__(self, num):
        self.num = num
        self.nxt = None
        self.prv = None
        allnodes.append(self)
 
    def insert(self, num):
        newn = Node(num)
        self.nxt = newn
        newn.prv = self
        newn.nxt = head
        head.prv = newn
        return newn
        
    def move_nxt(self, dir,ishead):
        node = self
        node.prv.nxt = node.nxt
        node.nxt.prv = node.prv 
        if dir:
            prv = node.nxt
            nxt = node.nxt.nxt
        else:
            prv = node.prv.prv
            nxt = node.prv
        prv.nxt = node
        node.prv = prv
        nxt.prv = node
        node.nxt = nxt
        if dir and ishead:
             return self.prv
        elif not dir and ishead:
             return self.nxt
        else:
             return self
         
def parse_input():
    global head,curr
    first = 1
    for line in sys.stdin:
        line = line.strip()
        if first:
           head = Node(int(line)) 
           curr = head
           first = 0
        else:
           curr = curr.insert(int(line))

def mix_once():
    global head,curr
    for i in range(len(allnodes)):
         times = (allnodes[i].num)%(len(allnodes)-1)
         curr = allnodes[i]
         for i in range(0,abs(times)):
             if times > 0:
                   if head == curr:
                       head = curr.move_nxt(1,1)
                   else:
                       curr = curr.move_nxt(1,0)
             else:
                   if head == curr:
                       head = curr.move_nxt(0,1)
                   else:
                       curr = curr.move_nxt(0,0)
    
def printit():
    global head
    curr = head
    for j in range(len(allnodes)):
         print(curr.num, end=' ')
         curr = curr.nxt
    print("\n")

def part(part):
    global head
    if part == 2:
        dkey = 811589153
        curr = head

        for j in range(len(allnodes)):
             curr = allnodes[j]
             curr.nxt = allnodes[(j+1) %len(allnodes)]
             curr.prv = allnodes[j-1]
             curr.num *=dkey
       
        for i in range(9):
            mix_once()
   
    mix_once() 

    curr = head
    ind0 = -1
    ct = 0
    for j in range(len(allnodes)):
         if not curr.num:
              ind0 = ct
         ct +=1
         curr = curr.nxt
   
    indices= []
    for i in [1000,2000,3000]:
        indices.append((ind0 + i)%len(allnodes))

    #printit()
    #print(ind0,indices)

    total = 0
    for j in range(0,len(allnodes)):
          if j in indices:
              total+=curr.num
          curr = curr.nxt
    
    return total


parse_input()
print(part(1))
print(part(2))
