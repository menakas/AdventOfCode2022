# https://adventofcode.com/2022/day/6
# Created by: Menaka S. 6 Dec 2022

import sys


line = sys.stdin.read()
def get_marker(line,length):
  chars = list(line)
  for i in range(0,len(chars)):
      if i>=length-1:
           if len(set(chars[i-length+1:i+1])) == length:
                return(i+1)

print(get_marker(line,4))
print(get_marker(line,14))
