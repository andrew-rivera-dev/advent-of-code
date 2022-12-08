from collections import Counter

line = open('2022/day6-data.txt').readline()

for i in range(4, len(line)):
    marker = line[i-4:i]
    counter = Counter(marker)
    if all(counter[c] == 1 for c in marker):
        print(i)
        break

