import fileinput

def doesContain(range1, range2):
    def contains(bigger, smaller):
        return bigger[0] <= smaller [0] and bigger[1] >= smaller[1]

    return contains(range1, range2) or contains(range2, range1)

total = 0

for line in fileinput.input(files ='2022/day4-data.txt'):
    a = line.rstrip().split(",")
    b = list(map(lambda pair: pair.split("-"), a))
    c = [list(map(int, x)) for x in b]

    if doesContain(c[0], c[1]):
        total += 1

print(total)