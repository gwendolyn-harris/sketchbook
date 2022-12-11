#!/usr/bin/env python3

from typing import Tuple
import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2021/day/11/input', cookies=cookie)

octopus_map = [[int(char) for char in line] for line in r.text.splitlines()]

# Part 1
# Naive approach
adjacent = [(0, 1), (1, 1), (1, 0), (1, -1), (-1, 0), (0, -1), (-1, 1), (-1, -1)]

# Just for fun
def pretty_print(energy_map:list[list[int]]) -> None:
    for line in energy_map:
        print("".join([str(num) if num != 0 else "\033[1m" + str(num) + "\033[0m" for num in line]))
    print(" ")

def process_step(energy_map: list[list[int]]) -> Tuple[int, list[list[int]]]:
    for i, line in enumerate(energy_map):
        for j, energy in enumerate(line):
            energy_map[i][j] += 1
    adjacent = [(0, 1), (1, 1), (1, 0), (1, -1), (-1, 0), (0, -1), (-1, 1), (-1, -1)]
    flashed = set()
    unflashed = True
    while unflashed == True:
        initial = len(flashed)
        for i, line in enumerate(energy_map):
            for j, energy in enumerate(line):
                if energy > 9 and (i, j) not in flashed:
                    unflashed == True
                    flashed.add((i, j))
                    for y, x in adjacent:
                        y_mov = i + y
                        x_mov = j + x
                        if y_mov >= 0 and y_mov < len(energy_map) and x_mov >= 0 and x_mov < len(line):
                            energy_map[y_mov][x_mov] += 1
        if len(flashed) == initial:
            unflashed = False
    for i, j in flashed:
        energy_map[i][j] = 0
    return (len(flashed), energy_map)

total = 0
pretty_print(octopus_map)
for i in range(100):
    flashes, octopus_map = process_step(octopus_map)
    pretty_print(octopus_map)
    total += flashes

print(total)
# My answer was 1665

# Part 2
all_flashed = False
step = 0
while all_flashed == False:
    step += 1
    flashes, octopus_map = process_step(octopus_map)
    if flashes == (len(octopus_map) * len(octopus_map[0])):
        all_flashed = True

print(100 + step)
# My answer was 235
