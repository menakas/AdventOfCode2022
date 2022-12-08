# https://adventofcode.com/2022/day/7
# Created by: Menaka S. 7 Dec 2022

import sys

allNodes = []

class Node:
 
    # Constructor to create a new node
    def __init__(self, name, size, type):
        self.children=[]
        self.name = name
        self.type = type
        self.size = size
        self.parent = None
        all.append(self)
 
    def insert(self, name, size, type = 'file'):
        child = Node(name,size,type)
        child.parent = self
        self.children.append(child)
        return self
        
    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def calc_size(self):
        if self.type == 'file':
           return self.size
        else:
           for child in self.children:
               self.size += child.calc_size()
           return self.size

    def print_children(self):
       for child in self.children:
           if child.type == 'file':
              print(child.name,child.size)
           else:
              print(child.name,child.size,child.type)
              child.print_children()

    def sum_children(self,sum):
       for child in self.children:
           if child.type == 'dir':
              sum = child.sum_children(sum)
              if child.size <=100000:
                 sum += child.size
       return sum

fsRoot =  Node('/',0,'dir')

for line in sys.stdin:
    line = line.strip()
    parts = line.split(' ')
    if parts[1] == 'cd' and parts[2] == '/':
       curr = fsRoot
    elif parts[1] == 'cd' and parts[2] == '..':
       curr = curr.parent
    elif parts[1] == 'cd':
       curr = curr.get_child(parts[2])
    elif parts[0] =='dir':
       curr = curr.insert(parts[1],0,'dir')
    elif parts[1] == 'ls':
       continue
    else:
       curr =curr.insert(parts[1],int(parts[0]),'file')


#Calculate size of directories
curr = fsRoot
curr.calc_size()

#For checking if tree is built properly
#curr = fsRoot
#curr.print_children()

#Part 1
curr = fsRoot
print(curr.sum_children(0))
print("===")

#Part 2
#print(fsRoot.size) 
toFreeup = 30000000-(70000000 - fsRoot.size)

print(min([i.size if i.size > toFreeup else 70000000 for i in allNodes ]))
