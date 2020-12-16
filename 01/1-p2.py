import sys
# three sum


def twosum(nums, target):
    setnums = set(nums)
    for num in nums:
        alt = target - num
        if alt in setnums:
            third_num = (target - 2020) * -1
            print(num, alt, third_num)
            print(num * alt * third_num)


f = open(sys.argv[1])

nums = []
for line in f.readlines():
    nums.append(int(line.strip()))

for num in nums:
    twosum(nums, 2020 - num)
