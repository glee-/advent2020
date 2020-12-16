import sys


def toboggan(geology, x_slope, y_slope):
    x = 0
    y = 0
    counts = 0
    for line in geology:
        if y % y_slope == 0:
            counts += geology[y][x % len(geology[0])] == '#'
            x += x_slope
        y += 1
    return counts


geology = []
f = open(sys.argv[1])
for line in f.readlines():
    geology.append(line.strip())

slopes = [
         [1, 1],
         [3, 1],
         [5, 1],
         [7, 1],
         [1, 2]
]

answer = 1

for slope in slopes:
    trees = toboggan(geology, slope[0], slope[1])
    answer *= trees
    print(slope, trees)
print(answer)
