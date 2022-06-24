film = input()
food = input()
tickets = int(input())

price = 0

if film == "John Wick":
    if food == "Drink":
        price = 12 * tickets
    elif food == "Popcorn":
        price = 15 * tickets
    else:
        price = 19 * tickets

elif film == "Star Wars":
    if food == "Drink":
        price = 18 * tickets
    elif food == "Popcorn":
        price = 25 * tickets
    else:
        price = 30 * tickets

    if tickets >= 4:
        price *= 0.7

else:
    if food == "Drink":
        price = 9 * tickets
    elif food == "Popcorn":
        price = 11 * tickets
    else:
        price = 14 * tickets

    if tickets == 2:
        price *= 0.85

print(f"Your bill is {price:.2f} leva.")
