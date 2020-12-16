import sys


def is_valid_password(pw, letter, min, max):
    counts = pw.count(letter)
    return counts >= min and counts <= max


f = open(sys.argv[1])

valid_passes = 0
for line in f.readlines():
    inputs = line.strip().split(' ')
    minmax = inputs[0].split('-')
    valid_passes += is_valid_password(inputs[2], inputs[1][0], int(minmax[0]),
                                      int(minmax[1]))

print(valid_passes)
