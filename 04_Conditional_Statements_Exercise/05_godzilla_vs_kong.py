def film_making(budget, extra, price):
    decor = budget * 0.1
    total_price_clothes = extra * price
    if extra > 150:
        total_price_clothes = total_price_clothes - total_price_clothes * 0.1
    diff = budget - decor - total_price_clothes
    if diff >= 0:
        print("Action!")
        print(f"Wingard starts filming with {diff:.2f} leva left.")
    else:
        diff = abs(diff)
        print("Not enough money!")
        print(f"Wingard needs {diff:.2f} leva more.")


budget = float(input())
extra = int(input())
price_clothes = float(input())

film_making(budget, extra, price_clothes)
