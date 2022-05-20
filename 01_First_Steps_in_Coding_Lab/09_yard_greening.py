yards = float(input())

price_per_squire_meter = 7.61

total_price = yards * price_per_squire_meter
discount = total_price * 18 / 100
price_after_discount = total_price - discount

print(f"The final price is: {price_after_discount:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")
