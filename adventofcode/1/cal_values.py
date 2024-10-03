import os

INPUT="adventofcode/1/input.txt"

# Read input lines
with open(INPUT, 'r') as f:
    cal_vals = [line.rstrip() for line in f]

setnums = []
for val in cal_vals:
    listval = list(val)
    nums = [n for n in listval if n.isdigit()]
    setnums.append(int(str(nums[0])+str(nums[-1])))

print(sum(setnums))


