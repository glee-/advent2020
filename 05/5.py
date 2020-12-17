import sys


def get_seat_id(boardingpass):
    reparsed_pass = ""
    for letter in boardingpass:
        if letter == "F" or letter == "L":
            reparsed_pass += "0"
        else:
            reparsed_pass += "1"
    row = int(reparsed_pass[:7], 2)
    col = int(reparsed_pass[7:], 2)
    seat = row * 8 + col
    return seat


f = open(sys.argv[1])
highest_id = -1
seats = []
for line in f.readlines():
    id = get_seat_id(line.strip())
    seats.append(id)
    if id > highest_id:
        highest_id = id
print(highest_id)

seats = sorted(seats)
prev = seats[0]
for seat in seats:
    if seat == prev + 2:
        print("Your seat is: ", prev + 1)
    prev = seat
