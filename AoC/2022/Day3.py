#!/usr/bin/env python3

import requests
import string

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2022/day/3/input', cookies=cookie)

priorities = dict(zip(string.ascii_letters, range(1, 53)))
sacks = r.text.splitlines()

# Part 1
shared_items = []
for ele in sacks:
    half = len(ele)//2
    comp1 = ele[:half]
    comp2 = ele[half:]
    shared_items.append(list(set(comp2) & set(comp1))[0])

total = 0
for char in shared_items:
    total += priorities[char]

print(total)
# I got 8240

# Part 2
badge_items = []
for i in range(len(sacks)//3):
    for char in sacks[i*3]:
        if char in sacks[i*3 + 1] and char in sacks[i*3 + 2]:
            badge_items.append(char)
            break

total = 0
for char in badge_items:
    total += priorities[char]

print(total)
# I got 2587
