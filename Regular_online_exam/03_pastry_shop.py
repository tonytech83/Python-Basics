cake_type = input()
cake_count = int(input())
purchase_day = int(input())

final_price = 0

if purchase_day <= 15:
    if cake_type == "Cake":
        final_price = cake_count * 24
    elif cake_type == "Souffle":
        final_price = cake_count * 6.66
    else:
        final_price = cake_count * 12.60
else:
    if cake_type == "Cake":
        final_price = cake_count * 28.70
    elif cake_type == "Souffle":
        final_price = cake_count * 9.80
    else:
        final_price = cake_count * 16.98

if purchase_day <= 22:
    if 100 <= final_price <= 200:
        final_price *= 0.85
    elif final_price > 200:
        final_price *= 0.75

if purchase_day <= 15:
    final_price *= 0.9

print(f"{final_price:.2f}")
