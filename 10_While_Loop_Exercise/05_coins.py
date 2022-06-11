resto = float(input())

change_to_coins = round(resto * 100)
coin_counter = 0

while change_to_coins != 0:
    if change_to_coins >= 200:
        change_to_coins -= 200
        coin_counter += 1
    elif change_to_coins >= 100:
        change_to_coins -= 100
        coin_counter += 1
    elif change_to_coins >= 50:
        change_to_coins -= 50
        coin_counter += 1
    elif change_to_coins >= 20:
        change_to_coins -= 20
        coin_counter += 1
    elif change_to_coins >= 10:
        change_to_coins -= 10
        coin_counter += 1
    elif change_to_coins >= 5:
        change_to_coins -= 5
        coin_counter += 1
    elif change_to_coins >= 2:
        change_to_coins -= 2
        coin_counter += 1
    elif change_to_coins >= 1:
        change_to_coins -= 1
        coin_counter += 1

print(coin_counter)
