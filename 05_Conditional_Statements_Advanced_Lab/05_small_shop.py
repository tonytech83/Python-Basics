item = input()
city = input()
quantity = float(input())

price = 0

if city == "Sofia":
    if item == "coffee":
        price = 0.5
    elif item == "water":
        price = 0.8
    elif item == "beer":
        price = 1.2
    elif item == "sweets":
        price = 1.45
    elif item == "peanuts":
        price = 1.6

if city == "Plovdiv":
    if item == "coffee":
        price = 0.4
    elif item == "water":
        price = 0.7
    elif item == "beer":
        price = 1.15
    elif item == "sweets":
        price = 1.3
    elif item == "peanuts":
        price = 1.5

if city == "Varna":
    if item == "coffee":
        price = 0.45
    elif item == "water":
        price = 0.7
    elif item == "beer":
        price = 1.1
    elif item == "sweets":
        price = 1.35
    elif item == "peanuts":
        price = 1.55

print(price * quantity)
