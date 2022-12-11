#!/usr/bin/env python3

import copy
import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2022/day/5/input', cookies=cookie)

# Part 1
og_stacks, moves = r.text.split("\n\n")
og_stacks = [row for row in og_stacks.splitlines()[0:-1]]
stacks = {i: [] for i in range(1, 10)}

for row in og_stacks:
    for i in range(0, len(row), 4):
        stacks[(i / 4) + 1].append(row[i + 1])

stacks = {stack: [crate for crate in crates[::-1] if crate.isalpha()] for stack, crates in stacks.items()}
moves = [tuple([int(word) for word in move.split() if word.isnumeric()]) for move in moves.splitlines()]

stacks_1 = copy.deepcopy(stacks)
stacks_2 = copy.deepcopy(stacks)

def move_crate(crate_map: dict[int, list[str]], init, end):
    crate_map[end].append(crate_map[init].pop())

for repeats, init, end in moves:
    for i in range(repeats):
        move_crate(stacks_1, init, end)

print("".join([stack[-1] for stack in stacks_1.values()]))
# I got QPJPLMNNR

# Part 2
def move_crates(crate_map: dict[int, list[str]], num, init, end):
    print(num, -num, crate_map[init][-num])
    crate_map[end].extend(crate_map[init][-num:])
    crate_map[init] = crate_map[init][:-num]

for num, init, end in moves:
    move_crates(stacks_2, num, init, end)

print("".join([stack[-1] for stack in stacks_2.values()]))
# I got BQDNWJPVJ

# utils
def pretty_print(crate_map):
    for stack, crates in crate_map.items():
        print(stack, ' :   ' + "".join(crates))
