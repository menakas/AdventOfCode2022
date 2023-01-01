# https://adventofcode.com/2022/day/16
# Created by: Menaka S. 16 Dec 2022

import sys
import re
from collections import deque

graph = dict()
frates = dict()

def get_release(times, start, lst, minsleft):
    release, curr = 0, start
    for valv in list(lst):
        minsleft -= (times[curr][valv] + 1)
        release += minsleft * frates[valv]
        curr = valv
    return release

def get_paths(valv):
    #Djikstra to calculate shortest path

    queue = deque([(0,valv)])
    times = {valv: 0}
    while queue:
        time, x = queue.popleft()
        for to, to_time in graph[x].items():
            if to not in times or time + to_time < times[to]:
                times[to] = time + to_time
                queue.append((times[to], to))
    #print(times)
    return times


# This function gives partial permutations of todo as well
# Though this seems to be wasteful for Part 1, it is useful for Part 1
# These partial permutations can be either of the path of me or the elephant 
def get_possible_permutations(times, todo, valv, opened, minsleft):
    for to in todo:
        newtime = times[valv][to] + 1
        if newtime < minsleft and newtime > 1:
            yield from get_possible_permutations(times, todo - {to}, to, opened + [to],minsleft - newtime)
    yield opened

def parse_input():
    pattern = re.compile(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.+)")
    for line in sys.stdin:
        mtch = pattern.match(line)
        if mtch:
            valv,frate,tovalvs = mtch.groups()
            frates[valv] = int(frate)
            tos = tovalvs.split(', ')
            graph[valv] = {to: 1 for to in tos}

    
parse_input()

all_times = {v: get_paths(v) for v in graph.keys() }# if v == 'AA' or frates[v]} #Djikstra
todo = {x for x in all_times if frates[x]}
       
total_release = max([get_release(all_times, 'AA', perm,30) for perm in get_possible_permutations(all_times,todo,'AA',[],30)])
print("Part 1:", total_release)

all_poss = [(perm,get_release(all_times, 'AA', perm,26)) for perm in get_possible_permutations(all_times,todo,'AA',[],26)]

sorted(all_poss,key = lambda x: x[1])

# Assuming that neither the elephant nor I shall contribute less than one third of the total release

mx = 0
#print(len(all_poss))
for i in range(len(all_poss)-1):
    if all_poss[i][1] < mx//3:
        continue
    for j in range(i+1,len(all_poss)):
       # ensuring that the same valves are not opened by me and the elephant
       if len(all_poss[j][0]) and not (set(all_poss[i][0]).intersection(set(all_poss[j][0]))):
           mx = max(mx,(all_poss[i][1] + all_poss[j][1]))
           #print(all_poss[i],all_poss[j],mx,all_poss[i][1] + all_poss[j][1])

print("Part 2:",mx)
