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
for i in range(preamble_len, len(nums)):
    retval = twoSum(nums[i-preamble_len:i], nums[i])
    if not retval:
        print(i, nums[i])
