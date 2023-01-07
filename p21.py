# https://adventofcode.com/2022/day/21
# Created by: Menaka S. 21 Dec 2022

import sys

monkeys = dict()
opmonkeys = dict()

def strip_last_char(word):
    return word[:-1] if word[-1] in ':,' else word
 
def parse_input():
    for line in sys.stdin:
         parts = list(map(strip_last_char,line.strip().split(' ')))
         if len(parts) == 2:
            monkeys[parts[0]] = int(parts[1])
         else:
            opmonkeys[parts[0]] = (parts[1],parts[2],parts[3])
    
def yell(mname):
   if mname in monkeys:
       return monkeys[mname]
   else:
       return eval(str(yell(opmonkeys[mname][0])) + opmonkeys[mname][1] + str(yell(opmonkeys[mname][2])))

def containshumn(mname):
    if mname in opmonkeys and (containshumn(opmonkeys[mname][0]) or containshumn(opmonkeys[mname][2])):
          return 1
    elif mname in monkeys and mname == 'humn':
          return 1
    return 0

def calchumn(mname,val):
    if mname in opmonkeys: 
        first = opmonkeys[mname][0]
        second = opmonkeys[mname][2]
        if containshumn(first):
            if opmonkeys[mname][1] == '+':
                return calchumn(first,val-yell(second))
            if opmonkeys[mname][1] == '-':
                return calchumn(first,val+yell(second))
            if opmonkeys[mname][1] == '*':
                return calchumn(first,val/yell(second))
            if opmonkeys[mname][1] == '/':
                return calchumn(first,val*yell(second))
        else:
            if opmonkeys[mname][1] == '+':
                return calchumn(second,val-yell(first))
            if opmonkeys[mname][1] == '-':
                return calchumn(second,yell(first)-val)
            if opmonkeys[mname][1] == '*':
                return calchumn(second,val/yell(first))
            if opmonkeys[mname][1] == '/':
                return calchumn(second,yell(first)/val)
    return val

def part1():
    return int(yell('root'))

def part2():
    first = opmonkeys['root'][0]
    second = opmonkeys['root'][2]
    if containshumn(first):
        val = yell(second)
        return int(calchumn(first,val))
    else:
        val = yell(first)
        return int(calchumn(second,val))
     

parse_input()
print(part1())
print(part2())
