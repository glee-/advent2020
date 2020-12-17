import sys


def get_counts(groupanswers):
    individuals = list(map(set, groupanswers))

    intersection = individuals[0]
    for individual in individuals:
        intersection = intersection & individual
    return len(intersection)


f = open(sys.argv[1])

groups = []
group = []
for line in f.readlines():
    stripped = line.strip()
    if stripped:
        group.append(stripped)
    else:
        groups.append(group)
        group = []
groups.append(group)

total = 0
for group in groups:
    total += get_counts(group)
print(total)
