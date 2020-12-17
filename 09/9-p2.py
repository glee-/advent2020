import sys


def twoSum(nums, target):
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return


f = open(sys.argv[1])
nums = []
for line in f.readlines():
    nums.append(int(line.strip()))

preamble_len = 25
target_num = -1
for i in range(preamble_len, len(nums)):
    retval = twoSum(nums[i-preamble_len:i], nums[i])
    if not retval:
        target_num = nums[i]

print(target_num)

idx = 0
distance = 1

while idx < len(nums):
    window = nums[idx:idx + distance]

    if sum(window) == target_num:
        print(window)
        print(min(window), max(window))
        print(min(window) + max(window))
        break
    elif sum(window) < target_num:
        distance += 1
    else:
        idx += 1
        distance = 1
