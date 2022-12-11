#!/usr/bin/env python3

from numpy import number
import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2021/day/8/input', cookies=cookie)

data = [string.split(" | ") for string in r.text.splitlines()]
output = [[''.join(sorted(string)) for string in row[1].split(' ')] for row in data]
signal_patterns = [[set(string) for string in row[0].split(' ')] for row in data]

total = 0
for row in output:
    for string in row:
        if len(string) == 2 or len(string) == 3 or len(string) == 4 or len(string) == 7:
            total += 1

print(total)
# My result was 369

output_sum = 0

for i, row in enumerate(signal_patterns):
    number_map = {8: {"a", "b", "c", "d", "e", "f", "g"}}
    letter_map = {}
    for ele in row:
        if len(ele) == 2:
            number_map[1] = ele
        if len(ele) == 4:
            number_map[4] = ele
        if len(ele) == 3:
            number_map[7] = ele
    letter_map["a"] = number_map[7] - number_map[1]
    for ele in row:
        if len(ele) == 6 and number_map[7].issubset(ele) and number_map[4].issubset(ele):
            letter_map["g"] = ele - number_map[7] - number_map[4]
            number_map[9] = ele
            break
    letter_map["e"] = number_map[8] - number_map[9]
    for ele in row:
        if len(ele) == 6 and (number_map[7]|letter_map["g"]|letter_map["e"]).issubset(ele):
            letter_map["b"] = ele - number_map[7] - letter_map["g"] - letter_map["e"]
            number_map[0] = ele
            break
    letter_map["d"] = number_map[8] - number_map[0]
    for ele in row:
        if len(ele) == 6 and ele is not number_map[0] and ele is not number_map[9]:
            number_map[6] = ele
            letter_map["c"] = number_map[8] - number_map[6]
            break
    letter_map["f"] = number_map[1] - letter_map["c"]
    number_map[2] = number_map[8] - letter_map["b"] - letter_map["f"]
    number_map[3] = number_map[8] - letter_map["b"] - letter_map["e"]
    number_map[5] = number_map[8] -letter_map["c"] - letter_map["e"]
    reverse_number_map = {''.join(sorted(value)): key for key, value in number_map.items()}
    output_sum += int(''.join([str(reverse_number_map[string]) for string in output[i]]))

print(output_sum)
# My result was 1031553
