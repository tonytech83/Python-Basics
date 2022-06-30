budget = float(input())
needed_gas_litters = float(input())
day = input()

guide_price = 100

total_price = 0

if day == "Saturday":
    total_price = (needed_gas_litters * 2.1 + guide_price) * 0.9
else:
    total_price = (needed_gas_litters * 2.1 + guide_price) * 0.8

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
