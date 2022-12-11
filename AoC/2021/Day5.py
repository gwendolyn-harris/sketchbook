#!/usr/bin/env python3

import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2021/day/5/input', cookies=cookie)
data = [line.split(" -> ") for line in r.text.splitlines()]

x1 = [int(line[0].split(',')[0]) for line in data]
y1 = [int(line[0].split(',')[1]) for line in data]
x2 = [int(line[1].split(',')[0]) for line in data]
y2 = [int(line[1].split(',')[1]) for line in data]

xmax = max(x2 + x1)
ymax = max(y2 + y1)

# Part 1
vent_map = [[0 for _ in range(xmax + 1)] for _ in range(ymax + 1)]
overlap_counter = 0

for i in range(len(data)):
    if x1[i] == x2[i]:
        for y in range(min(y1[i], y2[i]), max(y1[i], y2[i]) + 1):
            vent_map[y][x1[i]] += 1
            if vent_map[y][x1[i]] == 2:
                overlap_counter += 1
    elif y1[i] == y2[i]:
        for x in range(min(x1[i], x2[i]), max(x1[i], x2[i]) + 1):
            vent_map[y1[i]][x] += 1
            if vent_map[y1[i]][x] == 2:
                overlap_counter += 1

print(overlap_counter)
# My result: 6548

# Part 2
for i in range(len(data)):
    if x1[i] != x2[i] and y1[i] != y2[i]:
        xstep = 1 if x1[i] < x2[i] else -1
        ystep = 1 if y1[i] < y2[i] else -1
        for j, k in zip(range(x1[i], x2[i] + xstep, xstep), range(y1[i], y2[i] + ystep, ystep)):
            vent_map[k][j] += 1
            if vent_map[k][j] == 2:
                overlap_counter += 1

print(overlap_counter)
