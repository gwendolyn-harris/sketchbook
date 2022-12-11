#!/usr/bin/env python3

import requests
from typing import Tuple

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2021/day/13/input', cookies=cookie)

XMAX = 0
YMAX = 0
dot_list = []
for line in r.text.splitlines():
    if "fold along" not in line and line:
        pair = [int(num) for num in line.split(",")]
        if pair[0] > XMAX:
            XMAX = pair[0]
        if pair[1] > YMAX:
            YMAX = pair[1]
        dot_list.append(tuple(pair))

fold_list = [line.replace("fold along ", "") for line in r.text.splitlines() if "fold along" in line]
dot_map = [[False for _ in range(XMAX + 1)] for __ in range(YMAX + 1)]

for x, y in dot_list:
    dot_map[y][x] = True

def fold(fold: str, dot_map: list[list[bool]]) -> list[list[bool]]:
    axis, line = fold.split("=")
    if axis == "x":
        top = dot_map[:line]
        bottom = dot_map[line:]
        if len(top) > len(bottom):
            for i, y in enumerate(bottom.reversed()):
                for j, x in enumerate(y):
                    if top[-i][j] or x:
                        top[-1][j] = True
        else:
            for i, y in enumerate(top.reversed()):
                for j, x in enumerate(y)

# Part 1
