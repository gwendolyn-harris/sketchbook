#!/usr/bin/env python3

import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2022/day/9/input', cookies=cookie)

head_moves = [line.split()[0] for line in r.text.splitlines() for _ in range(int(line.split()[1]))]
tail_locs = set()
dir_map = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

def move_dir(dir: str, head_loc: tuple[int, int]) -> tuple[int, int]:
    h_x, h_y = head_loc
    move_x, move_y = dir_map[dir]
    return (h_x + move_x, h_y + move_y)

def tail_move(head_loc: tuple[int], tail_loc: tuple[int, int]) -> tuple[int, int]:
    h_x, h_y = head_loc
    t_x, t_y = tail_loc
    if h_x != t_x and h_y != t_y and (abs(h_x - t_x) > 1 or abs(h_y - t_y) > 1):
        return (t_x + (h_x - t_x)//abs(h_x - t_x), t_y + (h_y - t_y)//abs(h_y - t_y))
    elif h_x == t_x and abs(h_y - t_y) > 1:
        return (t_x, t_y + (h_y - t_y)//abs(h_y - t_y))
    elif h_y == t_y and abs(h_x - t_x) > 1:
        return (t_x + (h_x - t_x)//abs(h_x - t_x), t_y)
    else:
        return tail_loc

head_loc = (0, 0)
tail_loc = (0, 0)
for dir in head_moves:
    tail_locs.add(tail_loc)
    head_loc = move_dir(dir, head_loc)
    tail_loc = tail_move(head_loc, tail_loc)
tail_locs.add(tail_loc) # Adding the final position

print(len(tail_locs))
# I got 6563

# Part 2
knot_locs = set()
head_loc = (0, 0)
tail_knots = [(0, 0) for _ in range(9)]
for dir in head_moves:
    head_loc = move_dir(dir, head_loc)
    tail_knots[0] = tail_move(head_loc, tail_knots[0])
    for i in range(1, len(tail_knots)):
        tail_knots[i] = tail_move(tail_knots[i - 1], tail_knots[i])
    knot_locs.add(tail_knots[8])

print(len(knot_locs))
# I got 2653
