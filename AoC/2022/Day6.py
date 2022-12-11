#!/usr/bin/env python3

import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2022/day/6/input', cookies=cookie)

mem = [None] * 4
counter = 0

for char in r.text:
    mem.insert(0, char)
    mem.pop()
    if len(set(mem)) != 4 or None in mem:
        counter += 1
    else:
        counter += 1
        break

print(counter, mem)
# I got 1850

#Part 2

mem = [None] * 14
counter = 0
for char in r.text:
    mem.insert(0, char)
    mem.pop()
    if len(set(mem)) != 14 or None in mem:
        counter += 1
    else:
        counter += 1
        break

print(counter, mem)
