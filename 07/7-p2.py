import sys


def strip_s(bag):
    if bag[-1] == "s":
        return bag[:-1]
    return bag


def strip_num(bag):
    if bag[0].isnumeric():
        return bag[2:]
    return bag


def get_num(bag):
    if bag[0].isnumeric():
        return int(bag[0])
    return 0


mapping = {}


f = open(sys.argv[1])
for line in f.readlines():
    stripped = line.strip()[:-1]
    contains = stripped.split(" contain ")

    key = strip_s(contains[0])
    bag_items = [strip_s(bag) for bag in contains[1].split(", ")]
    bag_nums = [get_num(item) for item in bag_items]
    bag_vals = [strip_num(item) for item in bag_items]
    values = []
    for i in range(len(bag_nums)):
        values.extend(bag_nums[i] * [bag_vals[i]])

    if key not in mapping:
        mapping[key] = values
    else:
        mapping[key].extend(values)
        
root = "shiny gold bag"
# bfs
queue = [root]
nodes = 0
while queue:
    current_bag = queue.pop(0)
    nodes += 1
    if current_bag in mapping:
        queue.extend(mapping[current_bag])
print(nodes - 1)
