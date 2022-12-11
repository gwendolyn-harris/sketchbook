#!/usr/bin/env python3

import requests
import math
import copy

file = open("cookies.txt", "r")
cookie = dict(session=file.read().strip())
r = requests.get('https://adventofcode.com/2022/day/11/input', cookies=cookie)

monkeys = [[item.strip() for item in monkey.split("\n")] for monkey in r.text.split("\n\n")]

class Monkey:
    def __init__(self, monkey: list[str]):
        self.items = [int(item) for item in monkey[1].replace("Starting items:", "").split(", ")]
        self.operation = monkey[2].replace("Operation: new =", "")
        self.divisor = int(monkey[3].replace("Test: divisible by ", ""))
        self.truthy = int(monkey[4].replace("If true: throw to monkey ", ""))
        self.falsey = int(monkey[5].replace("If false: throw to monkey ", ""))
        self.inspections = 0

monkey_dict = dict()
for i, monkey in enumerate(monkeys):
    monkey_dict[i] = Monkey(monkey)

monkey_dict_1 = copy.deepcopy(monkey_dict)
monkey_dict_2 = copy.deepcopy(monkey_dict)

# Part 1
def run_a_round(monkeys: dict[int, Monkey]) -> None:
    for monkey in monkeys.values():
        while len(monkey.items) > 0:
            old = monkey.items.pop()
            new = eval(monkey.operation)
            monkey.inspections += 1
            new = new // 3
            if new % monkey.divisor == 0:
                monkeys[monkey.truthy].items.append(new)
            else:
                monkeys[monkey.falsey].items.append(new)

for _ in range(20):
    run_a_round(monkey_dict_1)

print(math.prod(sorted([monkey.inspections for monkey in monkey_dict_1.values()])[-2:]))
# I got 66124

# Part 2
lcm = math.lcm(*[monkey.divisor for monkey in monkey_dict_2.values()])
print(lcm)

def run_a_worried_round(monkeys: dict[int, Monkey]) -> None:
    for monkey in monkeys.values():
        while len(monkey.items) > 0:
            old = monkey.items.pop()
            new = eval(monkey.operation)
            monkey.inspections += 1
            new = new % lcm
            if new % monkey.divisor == 0:
                monkeys[monkey.truthy].items.append(new)
            else:
                monkeys[monkey.falsey].items.append(new)

for _ in range(10000):
    run_a_worried_round(monkey_dict_2)

print(math.prod(sorted([monkey.inspections for monkey in monkey_dict_2.values()])[-2:]))
# I got 19309892877
