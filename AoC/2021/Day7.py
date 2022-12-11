#!/usr/bin/env python3

import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2021/day/7/input', cookies=cookie)

data = [int(num) for num in r.text.split(',')]

# Part 1
positions = {}

for i in range(max(data)):
    positions[i] = 0
    for num in data:
        positions[i] += abs(num - i)

print(min(positions.values()))
# My result was 355521

# Part 2
positions2 = {}

for i in range(max(data)):
    positions2[i] = 0
    for num in data:
        n = abs(num - i)
        positions2[i] += (n*(n+1))//2

print(min(positions2.values()))
# My result was 100148777
