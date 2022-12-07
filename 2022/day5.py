import fileinput 

input = [
    ["G", "T", "R", "W"],
    ["G", "C", "H", "P", "M", "S", "V", "W"],
    ["C", "L", "T", "S", "G", "M"],
    ["J", "H", "D", "M", "W", "R", "F"],
    ["P", "Q", "L", "H", "S", "W", "F", "J"],
    ["P", "J", "D", "N", "F", "M", "S"],
    ["Z", "B", "D", "F", "G", "C", "S", "J"],
    ["B", "T", "R"],
    ["H", "N", "W", "L", "C"]
]

for line in fileinput.input(files='2022/day5-data.txt'):
    nums = [int(c) for c in line.rstrip().split(" ") if c.isnumeric()]
    quantity, source, destination = nums
    source = source - 1
    destination = destination - 1

    i = min(quantity, len(input[source]))
    while i > 0:
        crate = input[source].pop()
        input[destination].append(crate)
        i -= 1

final = []

for stack in input:
    final.append(stack.pop())

print(''.join(final))