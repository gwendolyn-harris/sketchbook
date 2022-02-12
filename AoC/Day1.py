# Day 1
import requests

file = open("cookies.txt", "r")

cookie = dict(session=file.read())

r = requests.get('https://adventofcode.com/2021/day/1/input', cookies=cookie)

data = [int(num) for num in r.text.splitlines()]

# Part 1
counter = 0

for i in range(len(data) - 1):
    if data[i+1] > data[i]:
        counter += 1

print(counter)
# Result for my data: 1832

# Part 2
counter = 0

for i in range(len(data)):
    if sum(data[i+1:i+4]) > sum(data[i:i+3]):
        counter += 1

print(counter)
# Result for my data: 1858