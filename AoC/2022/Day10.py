#!/usr/bin/env python3

import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2022/day/10/input', cookies=cookie)

commands = r.text.splitlines()

# Part 1
cycle = 1
cool_cycles = [20, 60, 100, 140, 180, 220]
strength_sum = 0
x = 1

def increment_cycle(cycle: int, x: int, strength_sum: int) -> tuple[int, int]:
    cycle += 1
    if cycle in cool_cycles:
        strength_sum += (x * cycle)
    return cycle, strength_sum

for command in commands:
    if command == 'noop':
        cycle, strength_sum = increment_cycle(cycle, x, strength_sum)
    elif command.split()[0] == 'addx':
        cycle, strength_sum = increment_cycle(cycle, x, strength_sum)
        dx = int(command.split()[1])
        x += dx
        cycle, strength_sum = increment_cycle(cycle, x, strength_sum)

print(strength_sum)
# I got 14040

# Part 2
screen = ['.' for _ in range(240)]
x = 1
cycle = 0

def draw_sprite(cycle: int, x: int, screen: list[str]) -> tuple[int, list[str]]:
    cycle += 1
    if cycle % 40 in range(x - 1, x + 2):
        screen[cycle] = '#'
    return (cycle, screen)

for command in commands:
    if command == 'noop':
        cycle, screen = draw_sprite(cycle, x, screen)
    elif command.split()[0] == 'addx':
        cycle, screen = draw_sprite(cycle, x, screen)
        dx = int(command.split()[1])
        x += dx
        cycle, screen = draw_sprite(cycle, x, screen)

buffer = []
for i, item in enumerate(screen, start=1):
    buffer.append(item)
    if i % 40 == 0:
        print("".join(buffer))
        buffer = []
