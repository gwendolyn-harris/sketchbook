#!/usr/bin/env python3

import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2021/day/10/input', cookies=cookie)

text = r.text.splitlines()

#Part 1

def get_first_error_score(string: str) -> int:
    stack = []
    symbol_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    symbol_pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
    for char in line:
        if char in symbol_pairs.values():
            stack.append(char)
        elif char in symbol_pairs.keys():
            if stack[-1] == symbol_pairs[char]:
                stack.pop()
            else:
                return symbol_scores[char]
    return 0

incomplete_lines = []
score = 0
for line in text:
    line_score = get_first_error_score(line)
    if line_score == 0:
        incomplete_lines.append(line)
    score += line_score

print(score)
# My answer was 323613

#Part 2
def get_completion_score(completion_string: str) -> int:
    symbol_scores = {")": 1, "]": 2, "}": 3, ">": 4}
    result = 0
    for symbol in completion_string:
        result = result * 5
        result += symbol_scores[symbol]
    return result

def get_completion_string(line: str) -> str:
    stack = []
    symbol_pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
    completion_pairs = {value: key for key, value in symbol_pairs.items()}
    for char in line:
        if char in symbol_pairs.values():
            stack.append(char)
        elif char in symbol_pairs.keys():
            for i, symbol in reversed(list(enumerate(stack))):
                if symbol == symbol_pairs[char]:
                    stack.pop(i)
                    break
    result = [completion_pairs[char] for char in stack]
    result.reverse()
    return result

line_scores = []
for line in incomplete_lines:
    line_scores.append(get_completion_score(get_completion_string(line)))

line_scores.sort()
print(line_scores[len(line_scores)//2])
# My answer was 3103006161
