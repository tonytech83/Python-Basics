budget = float(input())

product = input()
products_count = 0
products_price = 0

while product != "Stop":

    current_product_price = float(input())
    products_count += 1

    if products_count % 3 == 0:
        current_product_price *= 0.5

    if current_product_price > budget:
        budget -= current_product_price
        break

    budget -= current_product_price
    products_price += current_product_price

    product = input()

if product == "Stop":
    print(f"You bought {products_count} products for {products_price:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {abs(budget):.2f} leva!")
