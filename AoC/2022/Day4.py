#!/usr/bin/env python3

import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2022/day/4/input', cookies=cookie)

# Part 1

pairs = [[[int(num) for num in assignment.split("-")] for assignment in elf.split(",")] for elf in r.text.splitlines()]
sections = [tuple(set(range(assignments[0], assignments[1] + 1)) for assignments in elf) for elf in pairs]

counter = 0
for elf in sections:
    if elf[0] <= elf[1] or elf[0] >= elf[1]:
        counter += 1

print(counter)
# I got 569

# Part 2

counter = 0
for elf in sections:
    if not elf[0].isdisjoint(elf[1]):
        counter += 1

print(counter)
# I got 936
