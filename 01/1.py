import sys
# two sum


f = open(sys.argv[1])

nums = []
for line in f.readlines():
    nums.append(int(line.strip()))
setnums = set(nums)

for num in nums:
    alt = 2020 - num
    if alt in setnums:
        print(num, alt)
        print(num * alt)
