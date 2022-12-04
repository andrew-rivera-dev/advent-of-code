import fileinput

def does_overlap(range1, range2):
    s1 = set(range(range1[0], range1[1] + 1))
    s2 = set(range(range2[0], range2[1] + 1))

    return len(s1.intersection(s2)) > 0

total = 0

for line in fileinput.input(files ='2022/day4-data.txt'):
    clean = line.rstrip().split(",")
    split_hyphen = list(map(lambda pair: pair.split("-"), clean))
    cast_int = [list(map(int, x)) for x in split_hyphen]

    if does_overlap(cast_int[0], cast_int[1]):
        total += 1

print(total)