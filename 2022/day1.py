import fileinput
from collections import deque

biggest = [0,0,0]
curr = 0

for line in fileinput.input(files ='2022/day1-data.txt'):
    if line == "\n":
        small = min(biggest)
        if curr > small:
            i_small = biggest.index(small)
            biggest[i_small] = curr
        curr = 0
        continue
    curr += int(line)
    
print(sum(biggest))