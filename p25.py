# https://adventofcode.com/2022/day/25
# Created by: Menaka S. 25 Dec 2022

import sys

lst = []
def parse_input():
    for line in sys.stdin:
        lst.append(list(line.strip()))
   
def getval(num):

   val = 0
   for i in range(0,len(num)):
       if num[i] == '2':
           fv = 2
       if num[i] == '1':
           fv = 1
       if num[i] == '0':
           fv = 0
       if num[i] == '-':
           fv = -1
       if num[i] == '=':
           fv = -2
       pv = len(num) - i -1
       #print(pv,fv,val)
       val += (fv* (5 ** pv))
   #print(num,val)
   return val

def getsnafu(num): 
   placevalue = 1
   snafu = []
   while num != 0:
       remainder = num % (5 * placevalue)
       digit = remainder // placevalue
       #print(num,placevalue,digit,remainder)
       match digit:
           case 0 | 1 | 2:
               snafu.append(str(digit))
               num -= digit * placevalue
           case 3:
               snafu.append('=')
               num = num + 2 * placevalue
           case 4:
               snafu.append('-')
               num = num + placevalue

       placevalue *= 5

   snafu.reverse()
   #print(snafu)
   return ''.join(snafu)

def dopart():
   total = 0
   for i in range(len(lst)):
       total += getval(lst[i])
   print(total)
   return getsnafu(total)
       
parse_input()
print(dopart())

