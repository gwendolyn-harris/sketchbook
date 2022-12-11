#!/usr/bin/env python3

import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2022/day/2/input', cookies=cookie)

# Part 1
guide = [tuple(ele.split(" ")) for ele in r.text.splitlines()]

conversions = {'A': 'X', 'B': 'Y', 'C': 'Z'}
win_con = {'A': 'Y', 'B': 'Z', 'C': 'X'}
shape_score = {'X': 1, 'Y': 2, 'Z': 3}

def score_game(opponent: str, player: str) -> int:
    score = shape_score[player]

    if win_con[opponent] == player:
        return score + 6
    if player == conversions[opponent]:
        return score + 3
    else:
        return score

total_score = 0
for opponent, player in guide:
    total_score += score_game(opponent, player)

print(total_score)
# I got 13446

# Part 2
outcome_score = {'X': 0, 'Y': 3, 'Z': 6}
draw_con = {'A': 'X', 'B': 'Y', 'C': 'Z'}
loss_con = {'A': 'Z', 'B': 'X', 'C': 'Y'}
# could be more succinct in form {'A':(loss, draw, win), ...}

def new_score_game(opponent:str, outcome: str) -> int:
    score = outcome_score[outcome]
    if score == 0:
        return score + shape_score[loss_con[opponent]]
    if score == 3:
        return score + shape_score[draw_con[opponent]]
    else:
        return score + shape_score[win_con[opponent]]

new_total = 0
for opponent, outcome in guide:
    new_total += new_score_game(opponent, outcome)

print(new_total)
# I got 13509
