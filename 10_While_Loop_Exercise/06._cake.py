width = int(input())
length = int(input())

cake_pieces = width * length  # count of pieces
taken_pieces = 0

while taken_pieces < cake_pieces:
    current_take = input()
    if current_take == "STOP":
        break
    taken_pieces += int(current_take)

diff = abs(taken_pieces - cake_pieces)

if taken_pieces > cake_pieces:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")
