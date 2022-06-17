film_budget = float(input())
statistician_count = int(input())
price_clothes = float(input())

deckor_total = film_budget * 0.1
clothes_total = statistician_count * price_clothes
if statistician_count > 150:
    clothes_total = clothes_total * 0.9

total_spend = deckor_total + clothes_total

diff = abs(film_budget - total_spend)

if total_spend <= film_budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
