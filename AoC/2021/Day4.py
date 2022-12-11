#!/usr/bin/env python3

import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2021/day/4/input', cookies=cookie)
data = r.text.splitlines()

num_list = [int(num) for num in data.pop(0).split(",")]
board_rows = [[int(tile) for tile in row.split(" ") if tile != ''] for row in data if row != '']

class Board:
    def __init__(self, board):
        self.board = board
        self.bool_board = [[False for _ in range(5)] for _ in range(5)]
        self.won = False

    def mark_board(self, num):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == num:
                    self.bool_board[i][j] = True
                    self.did_i_win()
                    return

    def did_i_win(self):
        counter = {0:0, 1:0, 2:0, 3:0, 4:0}
        for row in self.bool_board:
            if all(row):
                self.won = True
                return
            for j, col in enumerate(row):
                if col:
                    counter[j] += 1
        if 5 in counter.values():
            self.won = True
            return
        else:
            return

    def get_final_score(self, last_call):
        total = 0
        for i, row in enumerate(self.bool_board):
            for j, col in enumerate(row):
                if not col:
                    total += self.board[i][j]
        return total*last_call

board_list = [Board(board_rows[i:i+5]) for i in range(0, len(board_rows), 5)]

# Part 1
def get_first_winner(board_list, num_list):
    for num in num_list:
        for board in board_list:
            board.mark_board(num)
            if board.won:
                return board.get_final_score(num)

print(get_first_winner(board_list, num_list))
# My result: 74320

# Part 2
def get_last_winner(board_list, num_list, num_won):
    winning_boards = num_won
    for num in num_list:
        for board in board_list:
            if not board.won:
                board.mark_board(num)
                if board.won:
                    winning_boards += 1
                    if winning_boards == len(board_list):
                        return board.get_final_score(num)

print(get_last_winner(board_list, num_list, 1))
# My result: 17884
