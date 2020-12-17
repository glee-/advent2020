import sys


def strip_s(bag):
    if bag[-1] == "s":
        return bag[:-1]
    return bag


def strip_num(bag):
    if bag[0].isnumeric():
        return bag[2:]
    return bag


reverse_mapping = {}


f = open(sys.argv[1])
for line in f.readlines():
    stripped = line.strip()[:-1]
    contains = stripped.split(" contain ")

    key = strip_s(contains[0])
    values = [strip_num(strip_s(bag)) for bag in contains[1].split(", ")]

    for value in values:
        if value not in reverse_mapping:
            reverse_mapping[value] = [key]
        else:
            reverse_mapping[value].append(key)

root = "shiny gold bag"
# bfs
queue = [root]
seen = set()
while queue:
    current_bag = queue.pop(0)
    if current_bag not in seen:
        seen.add(current_bag)
        if current_bag in reverse_mapping:
            queue.extend(reverse_mapping[current_bag])
print(len(seen) - 1)
