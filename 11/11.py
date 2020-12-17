import sys
import pprint as pp


def occupied_next(mapping, x, y):
    seats = ""
    seats += mapping[y-1][x-1:x+2]
    seats += mapping[y][x-1]
    seats += mapping[y][x+1]
    seats += mapping[y+1][x-1:x+2]
    adjacent = seats.count('#')
    current_seat = mapping[y][x]
    if adjacent >= 4 and current_seat == '#':
        return 'L'
    elif adjacent == 0 and current_seat == 'L':
        return '#'
    else:
        return current_seat


def add_padding(mapping):
    tmp_seating = []
    tmp_seating.append('.' * (width + 2))
    for row in mapping:
        tmp_seating.append('.' + row + '.')
    tmp_seating.append('.' * (width + 2))
    return tmp_seating


f = open(sys.argv[1])

seating_chart = []
for line in f.readlines():
    seating_chart.append(line.strip())

height = len(seating_chart)
width = len(seating_chart[0])

# add padding
seating_chart = add_padding(seating_chart)
# main loop
num_loops = 0
while True:
    new_chart = []
    for j in range(height):
        row = ""
        for i in range(width):
            seat = occupied_next(seating_chart, i + 1, j + 1)
            row += seat
        new_chart.append(row)
    new_chart = add_padding(new_chart)
    if new_chart == seating_chart:
        break
    else:
        seating_chart = new_chart
        num_loops += 1

occupied_seats = 0
for row in seating_chart:
    for seat in row:
        if seat == '#':
            occupied_seats += 1
print(occupied_seats)
