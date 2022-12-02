# Day 2: Submarine position

import fileinput

# count = {
#     "x" : 0,
#     "y" : 0,
# }

count = {
    "horizontal" : 0,
    "depth" : 0,
    "aim" : 0
}

for line in fileinput.input(files ='day2-data.txt'):
    direction, value = line.split()
    value = int(value)
    if direction == "forward":
        count["horizontal"] += value
        count["depth"] += count["aim"] * value
    elif direction == "up":
        count["aim"] -= value
    elif direction == "down":
        count["aim"] += value

print(count["horizontal"] * count["depth"])
