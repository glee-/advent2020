import sys


def is_valid_password(pw, letter, low, high):
    return (pw[low - 1] == letter) ^ (pw[high - 1] == letter)


f = open(sys.argv[1])

valid_passes = 0
for line in f.readlines():
    inputs = line.strip().split(' ')
    lowhigh = inputs[0].split('-')
    valid_passes += is_valid_password(inputs[2], inputs[1][0], int(lowhigh[0]),
                                      int(lowhigh[1]))

print(valid_passes)
