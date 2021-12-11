# Day 1: How many measurements are larger than the previous measurement?

# Part 1
import fileinput

nums = []
count = 0

for line in fileinput.input(files ='day1-data.txt'):
    nums.append(int(line))

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count += 1

print(count)

# Part 2