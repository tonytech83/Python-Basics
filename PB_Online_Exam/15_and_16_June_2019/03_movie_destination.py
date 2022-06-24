budget = float(input())
destination = input()
season = input()
days = int(input())

final_price = 0

if season == "Winter":
    if destination == "Dubai":
        final_price = 45000 * days * 0.7
    elif destination == "Sofia":
        final_price = 17000 * days * 1.25
    else:
        final_price = 24000 * days
else:
    if destination == "Dubai":
        final_price = 40000 * days * 0.7
    elif destination == "Sofia":
        final_price = 12500 * days * 1.25
    else:
        final_price = 20250 * days

diff = abs(budget - final_price)

if budget > final_price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
