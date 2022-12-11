#!/usr/bin/env python3

import requests
import copy

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2021/day/6/input', cookies=cookie)
data = [int(num) for num in r.text.split(",")]

data2 = copy.deepcopy(data)

# Naive approach
def lanternfish_counter(days, initial_list):
    for i in range(days):
        zeros = 0
        for j, num in enumerate(initial_list):
            if num == 0:
                zeros += 1
                initial_list[j] = 6
            else:
                initial_list[j] -= 1
        initial_list.extend([8 for _ in range(zeros)])
    return(len(initial_list))

print(lanternfish_counter(80, data))
# My result: 379414

# Performant approach (O(n) = n)
def efficient_lanternfish_counter(days, initial_list):
    fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for fish in initial_list:
        fish_dict[fish] += 1
    for _ in range(days):
        new_fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for fish, count in fish_dict.items():
            if fish == 0:
                new_fish_dict[8] = count
                new_fish_dict[6] = count
            else:
                new_fish_dict[fish - 1] += count
        fish_dict = new_fish_dict
    return(sum(fish_dict.values()))

print(efficient_lanternfish_counter(256, data2))
# My result: 1705008653296
