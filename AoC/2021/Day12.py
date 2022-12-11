#!/usr/bin/env python3

from typing import Set, Tuple
import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2021/day/12/input', cookies=cookie)

edges = [tuple(edge.split("-")) for edge in r.text.splitlines()]

map_dict = dict()
for edge in edges:
    for i, cave in enumerate(edge):
        if cave not in map_dict.keys():
            map_dict[cave] = set()
        map_dict[cave].add(edge[i - 1])

# Part 1
def get_unique_paths(map_dict: dict, current_cave: str, current_path: Tuple[str], path_set: Set[Tuple[str]]) -> Set[Tuple[str]]:
    if current_cave != "end":
        for cave in map_dict[current_cave]:
            if cave.isupper() or cave not in current_path:
                get_unique_paths(map_dict, cave, tuple(list(current_path) + [cave]), path_set)
    else:
        path_set.add(current_path)
    return path_set

unique_path_set = get_unique_paths(map_dict, "start", ("start",), set())

print(len(unique_path_set))
# My answer was 4011

# Part 2
def get_paths(map_dict: dict, current_cave: str, current_path: Tuple[str], path_set: Set[Tuple[str]]) -> Set[Tuple[str]]:
    if current_cave != "end":
        for cave in map_dict[current_cave]:
            if cave.isupper() or cave not in current_path:
                get_paths(map_dict, cave, tuple(list(current_path) + [cave]), path_set)
            elif cave != "start":
                has_double = False
                for visited in current_path:
                    if visited.islower() and current_path.count(visited) > 1:
                        has_double = True
                        break
                if not has_double:
                    get_paths(map_dict, cave, tuple(list(current_path) + [cave]), path_set)
                    continue
    else:
        path_set.add(current_path)
    return path_set

path_set = get_paths(map_dict, "start", ("start",), set())

print(len(path_set))
