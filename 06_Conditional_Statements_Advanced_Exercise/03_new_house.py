flower_type = input()
count = int(input())
budget = int(input())

price = 0

if flower_type == "Roses":
    price = 5
    if count > 80:
        price *= 0.9
elif flower_type == "Dahlias":
    price = 3.8
    if count > 90:
        price *= 0.85
elif flower_type == "Tulips":
    price = 2.8
    if count > 80:
        price *= 0.85
elif flower_type == "Narcissus":
    price = 3
    if count < 120:
        price *= 1.15
else:  # check for Gladiolus
    price = 2.5
    if count < 80:
        price *= 1.2

total_price = price * count
diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {count} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
