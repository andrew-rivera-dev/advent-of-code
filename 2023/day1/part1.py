import fileinput
from functools import reduce

def filterDigits(line):
    return list(filter(lambda char: char.isdigit(), line))

digitsArrs = []

for line in fileinput.input(files ='2023/day1/input.txt'):
    digits = list(filter(filterDigits, line))
    digitsArrs.append(digits)

calibrations = []

for arr in digitsArrs:
    first = arr[0]
    second = arr[-1]
    calibrations.append(int(first + second))

print(sum(calibrations))