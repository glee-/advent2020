import sys


def get_counts(groupanswers):
    return len(set(groupanswers))


f = open(sys.argv[1])

groups = []
group = ""
for line in f.readlines():
    stripped = line.strip()
    if stripped:
        group += stripped
    else:
        groups.append(group)
        group = ""
groups.append(group)

total = 0
for group in groups:
    total += get_counts(group)
print(total)
