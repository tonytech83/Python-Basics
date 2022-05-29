age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

toys = 0
money = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        money += (10 * year / 2) - 1
    else:
        toys += 1

total_money = money + (toys * price_per_toy)
diff = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
