#!/usr/bin/env python3

import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2022/day/7/input', cookies=cookie)

history = [tuple(line.split()) for line in r.text.splitlines()]
dir_tree = dict()

def access_cwd(tree: dict, cwd: str):
    for dirr in cwd.split("."):
        if dirr in tree:
            tree = tree[dirr]
    return tree

command_mem = ""
cwd = ""
for line in history:
    if line[0] == "$":
        command_mem = line[1]
        if line[1] == "cd":
            if line[2] == "..":
                cwd = ".".join(cwd.split(".")[:-2]) + "."
            else:
                cwd += (line[2] + ".")
                access_cwd(dir_tree, cwd)[line[2]] = dict()
        elif line[1] == "ls":
            pass
    elif line[0] == "dir":
        pass
    elif line[0].isnumeric():
        access_cwd(dir_tree, cwd)[line[1]] = line[0]

def get_dir_sizes(tree: dict, dir_sizes: dict, cwd="") -> int:
    total_size = 0
    for k, v in tree.items():
        if type(v) == dict:
            total_size += get_dir_sizes(v, dir_sizes, (cwd + "." + k))
        else:
            total_size += int(v)
    dir_sizes[cwd] = total_size
    return total_size

dir_sizes = dict()
get_dir_sizes(dir_tree, dir_sizes)

print(sum([num for num in dir_sizes.values() if num <= 100000]))
# I got 1723892

# Part 2
print(sorted([size for size in dir_sizes.values() if 70000000 - dir_sizes["./"] + size >= 30000000])[0])

#util
def pretty_print(tree: dict, indents=0):
    for k, v in tree.items():
        if type(v) == dict:
            print(indents * " " + "-" + k)
            indents += 1
            pretty_print(v, indents)
        else:
            print(indents * " " + k, v)
