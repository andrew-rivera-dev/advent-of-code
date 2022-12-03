import fileinput
import string

itemTypes = string.ascii_lowercase + string.ascii_uppercase

def calculatePriority(itemType):
    return itemTypes.index(itemType) + 1

def findCommonItemType(c1, c2, c3):
    return list(set(c1).intersection(set(c2)).intersection(set(c3)))[0]

total = 0
rucksackGroup = []

for line in fileinput.input(files ='2022-day3-data.txt'):
    rucksackGroup.append(line.rstrip())
    if len(rucksackGroup) == 3:
        commonItemType = findCommonItemType(rucksackGroup[0], rucksackGroup[1], rucksackGroup[2])
        total += calculatePriority(commonItemType)
        rucksackGroup = []

print(total)