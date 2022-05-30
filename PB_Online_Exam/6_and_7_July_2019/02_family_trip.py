budget = float(input())
overnight_count = int(input())
price_per_overnight = float(input())
additional_costs = int(input())

total_cost = 0

if overnight_count <= 7:
    total_cost = overnight_count * price_per_overnight + (budget * additional_costs / 100)
else:
    total_cost = overnight_count * (price_per_overnight * 0.95) + (budget * additional_costs / 100)

diff = abs(budget - total_cost)

if budget >= total_cost:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
