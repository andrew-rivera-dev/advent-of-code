# Day 1: Sonar Sweep

import fileinput

nums = []
count = 0

for line in fileinput.input(files ='day1-data.txt'):
    nums.append(int(line))

# Part 1

# for i in range(1, len(nums)):
#     if nums[i] > nums[i-1]:
#         count += 1

# print(count)

# Part 2

for i in range(0, len(nums) - 3):
    r1 = sum(nums[i:i+3])
    r2 = sum(nums[i+1:i+4])

    if r1 < r2:
        count += 1

print(count)
