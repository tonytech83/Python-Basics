month = input()
nights_count = int(input())

range_1 = ["May", "October"]
range_2 = ["June", "September"]
range_3 = ["July", "August"]

price_apartment = 0
price_studio = 0

if month in range_1:
    price_studio = nights_count * 50
    price_apartment = nights_count * 65
    if 7 < nights_count <= 14:
        price_studio *= 0.95
    elif nights_count > 14:
        price_studio *= 0.7
        price_apartment *= 0.9

elif month in range_2:
    price_studio = nights_count * 75.2
    price_apartment = nights_count * 68.7
    if nights_count > 14:
        price_studio *= 0.8
        price_apartment *= 0.9

elif month in range_3:
    price_studio = nights_count * 76
    price_apartment = nights_count * 77
    if nights_count > 14:
        price_apartment *= 0.9

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
