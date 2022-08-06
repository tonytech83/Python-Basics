from math import ceil

guests_count = int(input())
budget = int(input())

cake_count = ceil(guests_count / 3)
eggs_count = guests_count * 2

total_price = cake_count * 4 + eggs_count * 0.45

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'Lyubo bought {cake_count} Easter bread and {eggs_count} eggs.')
    print(f'He has {diff:.2f} lv. left.')
else:
    print(f"Lyubo doesn't have enough money.")
    print(f'He needs {diff:.2f} lv. more.')
