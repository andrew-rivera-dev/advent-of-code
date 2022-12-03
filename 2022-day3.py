import fileinput
import string

itemTypes = string.ascii_lowercase + string.ascii_uppercase

def calculatePriority(itemType):
    return itemTypes.index(itemType) + 1

def findCommonItemType(c1, c2):
    return list(set(c1).intersection(set(c2)))[0]

total = 0

for line in fileinput.input(files ='2022-day3-data.txt'):
    clean = line.rstrip()
    leftsplit = len(clean) // 2 - 1
    compartment1 = line[0:leftsplit+1]
    compartment2 = line[leftsplit+1:]
    commonItemType = findCommonItemType(compartment1, compartment2)
    total += calculatePriority(commonItemType)

print(total)