test_data = []
with open("./test.txt", "r") as file:
    for line in file:
        test_data.append(line)

data = []
with open("./input.txt", "r") as file:
    for line in file:
        data.append(line)

def find_seat_id(data):
    seat_ids = []
    for seat in data:
        row_range, seat_range = (0,127), (0,7)
        for c in seat:
            if c == 'F':
                l, h = row_range
                row_range = l, (h-l)//2 + l 
            elif c == 'B':
                l, h = row_range
                row_range = (h+l)//2+1, h
            if c == 'L':
                l, h = seat_range
                seat_range = l, (h-l)//2 + l 
            elif c == 'R':
                l, h = seat_range
                seat_range = (h+l)//2+1, h

        seat_ids.append(row_range[0] * 8 + seat_range[0])
    return seat_ids

print("**** Tests *****")
print(find_seat_id(test_data))
assert [567, 119, 820] == find_seat_id(test_data)
print("**** Part 1 *****")
all_seats = find_seat_id(data)
print("Max seat ID:", max(all_seats))

print("**** Part 2 *****")
sorted_seats = sorted(all_seats)
a,b,*rest = sorted_seats
while not a+1 == b-1:
    a,b,*rest = [*rest]

assert a+1 == b-1
print("Your seat:", a+1)

