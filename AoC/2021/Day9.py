#!/usr/bin/env python3

import math
import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2021/day/9/input', cookies=cookie)

# Part 1
HEIGHTMAP = [[int(char) for char in line] for line in r.text.splitlines()]
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
risk_level = 0
low_points = []

def is_low_point(heightmap: list[list[int]], i: int, j: int) -> bool:
    for k, l in DIRECTIONS:
        y_mov = i + k
        x_mov = j + l
        if 0 <= y_mov and y_mov <= len(HEIGHTMAP) - 1 and 0 <= x_mov and x_mov <= len(row) - 1 and HEIGHTMAP[y_mov][x_mov] <= HEIGHTMAP[i][j]:
            return False
    return True

# record low points (for Part 2) and get sum of risk levels of each
for i, row in enumerate(HEIGHTMAP):
    for j, height in enumerate(row):
        if is_low_point(HEIGHTMAP, i, j):
            risk_level += (1 + height)
            low_points.append((i, j))

print(risk_level)
# My answer was 594

# Part 2
def get_basin(heightmap: list[list[int]], low_point: tuple[int, int], basin: set) -> set:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    i, j = low_point
    for k, l in directions:
        y_mov = i + k
        x_mov = j + l
        if 0 <= y_mov and y_mov < len(HEIGHTMAP) and 0 <= x_mov and x_mov < len(row):
            if (y_mov, x_mov) in basin or heightmap[y_mov][x_mov] == 9:
                continue
            else:
                basin.add((y_mov, x_mov))
                basin = get_basin(heightmap, (y_mov, x_mov), basin)
    return basin

basin_sizes = []

for low_point in low_points:
    basin = get_basin(HEIGHTMAP, low_point, {low_point})
    basin_sizes.append(len(basin))

basin_sizes.sort()
print(math.prod(basin_sizes[-3:]))
# My answer was 858494
