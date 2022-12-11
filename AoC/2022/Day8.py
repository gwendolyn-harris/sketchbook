#!/usr/bin/env python3

import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2022/day/8/input', cookies=cookie)

tree_grid = [[int(char) for char in line] for line in r.text.splitlines()]

def vert_slice(grid: list[list[int]], x: int) -> list:
    return [row[x] for row in grid]

# Part 1
def is_visible(grid: list[list[int]], x: int, y: int) -> bool:
    tree_height = tree_grid[y][x]
    return (max(grid[y][x + 1:]) < tree_height or max(grid[y][:x]) < tree_height \
       or max(vert_slice(grid, x)[y + 1:]) < tree_height or max(vert_slice(grid, x)[:y]) < tree_height)

count = len(tree_grid) * 2 + len(tree_grid[0]) * 2 - 4
for y in range(1, len(tree_grid) - 1):
    for x in range(1, len(tree_grid[y]) - 1):
        if is_visible(tree_grid, x, y):
            count += 1

print(count)
# I got 1870

# Part 2
def get_viewing_distance(line: list[int], tree_height: int) -> int:
    count = 0
    for tree in line:
        if tree < tree_height:
            count += 1
        else:
            return count + 1
    return count

def get_score(grid: list[list[int]], x: int, y: int) -> int:
    tree_height = grid[y][x]
    return get_viewing_distance(grid[y][x + 1:], tree_height) * get_viewing_distance(grid[y][:x][::-1], tree_height) * \
        get_viewing_distance(vert_slice(grid, x)[y + 1:], tree_height) * get_viewing_distance(vert_slice(grid, x)[:y][::-1], tree_height)

scores = [get_score(tree_grid, x, y) for x in range(len(tree_grid[0])) for y in range(len(tree_grid))]

print(max(scores))
# I got 517440
