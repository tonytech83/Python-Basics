strawberry_price_kg = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberry = float(input())

strawberry_price = strawberry * strawberry_price_kg
raspberries_price = raspberries * strawberry_price_kg * 0.5
oranges_price = oranges * strawberry_price_kg * 0.5 * 0.6
bananas_price = bananas * strawberry_price_kg * 0.5 * 0.2

total_price = strawberry_price + raspberries_price + oranges_price + bananas_price

print(f"{total_price:.2f}")

