# Day 3: Binary Diagnostic - break

import fileinput

# Part 1

count = {}

for num in fileinput.input(files ='day3-data.txt'):
    for i in range(len(num) - 1): # shorten each number by one digit to remove newline chars
        if i in count:
            if num[i] == "0":
                count[i] -= 1
            else:
                count[i] += 1
        else:
            if num[i] == "0":
                count[i] = -1
            else:
                count[i] = 1

gamma = ""
epsilon = ""

for key, value in count.items():
    if value > 0:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))