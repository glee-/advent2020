import sys

f = open(sys.argv[1])
adapters = []
for line in f.readlines():
    adapters.append(int(line.strip()))
adapters.append(0)
adapters = sorted(adapters)
adapters.append(adapters[-1] + 3)

memoize = {}
memoize[adapters[0]] = 1

for adapter in adapters[1:]:
    nums = [i for i in range(adapter - 3, adapter)]
    connections = 0
    for num in nums:
        if num in memoize:
            connections += memoize[num]
    memoize[adapter] = connections
print(memoize[adapters[-1]])
