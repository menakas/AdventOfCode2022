# https://adventofcode.com/2022/day/19
# Created by: Menaka S. 19 Dec 2022
# This is a modified version from what I originally submitted inspired by ideas from the subreddit
# This runs relatively faster due to optimizations

import sys
from collections import deque

def parse_and_solve():
    ct = 0
    total = 0
    prod = 1
    for line in sys.stdin:
        parts = line.strip().split(' ')
        bpid = int(parts[1][:-1])
        mxgeodes = get_max_geodes(int(parts[6]), int(parts[12]), int(parts[18]), int(parts[21]), int(parts[27]), int(parts[30]),24)
        total += (bpid * mxgeodes)
        if ct < 3:
            prod *= get_max_geodes(int(parts[6]), int(parts[12]), int(parts[18]), int(parts[21]), int(parts[27]), int(parts[30]),32)
        ct += 1
    return (total,prod)

def get_max_geodes(ore_cost_ore, clay_cost_ore, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_obsidian, minutes_left):
    best = 0 
    max_ore_cost = max([ore_cost_ore, clay_cost_ore, obsidian_cost_ore, geode_cost_ore])

    queue = deque([(0, 0, 0, 0, 1, 0, 0, 0, minutes_left)])
    seen = set()

    while queue:
        ores, clays, obsidians, geodes, ore_robots, clay_robots, obsidian_robots, geode_robots, minutes_left = queue.popleft()

        best = max(best, geodes)

        if minutes_left == 0:
            continue


        # Some optimizations to make the code run faster

        # We can atmost spend only max_ore_cost number of ores per minute. So, get rid of more ore robots
        if ore_robots >= max_ore_cost:
            ore_robots = max_ore_cost
        # We can atmost spend only obsidian_cost_clay number of clays per minute. So, get rid of more clay robots
        if clay_robots >= obsidian_cost_clay:
            clay_robots = obsidian_cost_clay 
        # We can atmost spend only geode_cost_obsidian number of obsidians per minute. So, get rid of more obsidian robots
        if obsidian_robots >= geode_cost_obsidian:
            obsidian_robots = geode_cost_obsidian 

        # Get rid of more ores that may never be used
        # At max, we may spend max_ore_cost for each minute left, and ore robots produce 1 for every minute left. 
        if ores >= (max_ore_cost * minutes_left) - ore_robots * (minutes_left - 1):
            ores = (max_ore_cost * minutes_left) - ore_robots * (minutes_left - 1)
        # Get rid of more clays than may ever be used
        if clays >= (obsidian_cost_clay * minutes_left) - clay_robots * (minutes_left - 1):
            clays = (obsidian_cost_clay * minutes_left) - clay_robots * (minutes_left - 1)
        # Get rid of more obsidians than may ever be used
        if obsidians >=(geode_cost_obsidian * minutes_left) - obsidian_robots * (minutes_left - 1):
            obsidians = (geode_cost_obsidian * minutes_left) - obsidian_robots * (minutes_left - 1)


        if (ores, clays, obsidians, geodes, ore_robots, clay_robots, obsidian_robots, geode_robots, minutes_left) in seen:
            continue
        seen.add((ores, clays, obsidians, geodes, ore_robots, clay_robots, obsidian_robots, geode_robots, minutes_left))

        # Don't buy anything
        queue.append((ores + ore_robots, clays + clay_robots, obsidians + obsidian_robots, geodes + geode_robots, ore_robots, clay_robots, obsidian_robots, geode_robots, minutes_left-1))

        # Buy Ore Robot
        if ores>=ore_cost_ore:
            queue.append((ores-ore_cost_ore + ore_robots, clays + clay_robots, obsidians + obsidian_robots, geodes + geode_robots, ore_robots + 1, clay_robots, obsidian_robots, geode_robots, minutes_left-1))

        # Buy Clay Robot
        if ores>=clay_cost_ore: 
            queue.append((ores-clay_cost_ore + ore_robots, clays + clay_robots, obsidians + obsidian_robots, geodes + geode_robots, ore_robots, clay_robots + 1, obsidian_robots, geode_robots, minutes_left-1))

        # Buy Obsidian Robot
        if ores>=obsidian_cost_ore and clays>=obsidian_cost_clay:
            queue.append((ores-obsidian_cost_ore + ore_robots, clays-obsidian_cost_clay + clay_robots, obsidians + obsidian_robots, geodes + geode_robots, ore_robots, clay_robots, obsidian_robots + 1, geode_robots, minutes_left-1))

        # Buy Geode Robot
        if ores>=geode_cost_ore and obsidians>=geode_cost_obsidian:
            queue.append((ores-geode_cost_ore + ore_robots, clays + clay_robots, obsidians-geode_cost_obsidian + obsidian_robots, geodes + geode_robots, ore_robots, clay_robots, obsidian_robots, geode_robots + 1, minutes_left-1))

    return best


part1, part2 = parse_and_solve()
print("Part 1:", part1)
print("Part 2:", part2)
