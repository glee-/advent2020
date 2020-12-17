import sys

f = open(sys.argv[1])
adapters = []
for line in f.readlines():
    adapters.append(int(line.strip()))
adapters.append(0)
adapters = sorted(adapters)
adapters.append(adapters[-1] + 3)
print(adapters)

diffs = []
for i in range(len(adapters) - 1):
    diffs.append(adapters[i + 1] - adapters[i])
ones = diffs.count(1)
threes = diffs.count(3)
print(diffs)
print(ones, threes)
print(ones * threes)
