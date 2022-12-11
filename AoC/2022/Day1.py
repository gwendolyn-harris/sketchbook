#!/usr/bin/env python3

import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2022/day/1/input', cookies=cookie)

# Part 1
outer_list = []
inner_list = []
for ele in r.text.splitlines():
    if ele:
        inner_list.append(int(ele))
    else:
        outer_list.append(inner_list)
        inner_list = []

sums = [sum(wares) for wares in outer_list]

print(max(sums))
# I got 67450

# Part 2

print(sum(sorted(sums)[-3:]))
# I got 199357
