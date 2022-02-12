# Day 2
import requests

file = open("cookies.txt", "r")

cookie = dict(session=file.read())

r = requests.get('https://adventofcode.com/2021/day/2/input', cookies=cookie)

data = [directive.split() for directive in r.text.splitlines()]

# Part 1
x_position = 0

depth = 0

for directive in data:
    if directive[0] == "forward":
        x_position += int(directive[1])
    elif directive[0] == "down":
        depth += int(directive[1])
    else:
        depth = depth - int(directive[1])

print(depth*x_position)
# Result for my data: 1694130

# Part 2
aim = 0

x_position = 0

depth = 0

for directive in data:
    if directive[0] == "forward":
        x_position += int(directive[1])
        depth += aim * int(directive[1])
    elif directive[0] == "down":
        aim += int(directive[1])
    else:
        aim = aim - int(directive[1])

print(depth*x_position)
#Result for my data: 1698850445