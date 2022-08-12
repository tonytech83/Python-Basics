vegetables_price = float(input())
fruit_price = float(input())
vegetables_kg = int(input())
fruit_kg = int(input())

total_veg_price = vegetables_kg * vegetables_price
total_fruit_price = fruit_kg * fruit_price

total = (total_fruit_price + total_veg_price) / 1.94

print(f'{total:.2f}')
