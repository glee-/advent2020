import sys


x = 0
counts = 0
f = open(sys.argv[1])
for line in f.readlines():
    inputline = line.strip()
    counts += inputline[x % len(inputline)] == '#'
    x += 3
print(counts)
