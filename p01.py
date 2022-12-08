# https://adventofcode.com/2022/day/1
# Created by: Menaka S. 1 Dec 2022

import sys

ct = 0
sum = 0
food = []
for line in sys.stdin:
    line = line.strip()
    if line == "":
        food.append(sum)
        sum = 0 
        ct +=1
    else:
        sum += int(line)
       
food.append(sum)

total = 0
mx = max(food)
total += mx
food.remove(mx)

mx = max(food)
total += mx
food.remove(mx)

mx = max(food)
total += mx
food.remove(mx)

print(total)
