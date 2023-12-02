import fileinput
from functools import reduce

def doesKeyMatch(line, index, key):
    charsToEndOfLine = len(line) - (index + len(key))
    
    endIndex = index + len(key)

    if index + len(key) > len(line):
        endIndex = index + charsToEndOfLine + 1

    substrToMatch = line[index:endIndex]
    
    return substrToMatch == key

def filterDigits(line):
    word_to_digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    result = []
    currentWord = ""

    for index, char in enumerate(line):
        if char.isalpha():
            for key in word_to_digit.keys():
                if doesKeyMatch(line, index, key):
                    result.append(word_to_digit[key])
        else:
            if char.isdigit(): result.append(char)
    
    return result

calibrationArr = []

for line in fileinput.input(files ='2023/day1/input.txt'):
    digits = filterDigits(line)
    first = digits[0]
    second = digits[-1]
    calibrationArr.append(int(first + second))

print(sum(calibrationArr))
