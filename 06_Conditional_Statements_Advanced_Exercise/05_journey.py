budget = float(input())
season = input()

price = 0
where = "Hotel"
destination = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
        where = "Camp"
    elif season == "winter":
        price = budget * 0.7

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
        where = "Camp"
    elif season == "winter":
        price = budget * 0.8

else:
    destination = "Europe"
    price = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{where} - {price:.2f}")
