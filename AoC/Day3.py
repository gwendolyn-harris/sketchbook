import requests

file = open("cookies.txt", "r")
cookie = dict(session=file.read())
r = requests.get('https://adventofcode.com/2021/day/3/input', cookies=cookie)
data = r.text.splitlines()

# Part 1
def get_common_at_index(data, index, find_most_common):
    total = 0
    for num in data:
        total += int(num[index])
        half_length = len(data)/2
    if (find_most_common and total >= half_length) or (find_most_common and total < half_length):
        return "1"
    else:
        return "0"

most_common_digits = []
least_common_digits = []

for index in range(len(data[0])):
    most_common_digits.append(get_common_at_index(data, index, True))
    least_common_digits.append(get_common_at_index(data, index, False))

gamma = int("".join(most_common_digits), 2)
epsilon = int("".join(least_common_digits), 2)
print(gamma*epsilon)
# My result: 2035764


# Part 2
def filter_data(data, find_most_common):
    new_data = data
    for index in range(len(data[0])):
        print(index)
        if len(new_data) == 1:
            break
        new_data = [num for num in new_data if num[index] == get_common_at_index(new_data, index, find_most_common)]
    return int(new_data[0], 2)

O2_rating = filter_data(data, True)
CO2_rating = filter_data(data, False)
print(O2_rating*CO2_rating)
# My result: 2817661