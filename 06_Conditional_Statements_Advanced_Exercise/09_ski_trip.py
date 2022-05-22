nights_count = int(input()) - 1
room_type = input()
rating = input()

discount = 0
price = 0

if room_type == "room for one person":
    price = nights_count * 18

elif room_type == "apartment":
    if nights_count < 10:
        discount = 0.7
    elif 10 <= nights_count <= 15:
        discount = 0.65
    else:
        discount = 0.5
    price = nights_count * 25 * discount

elif room_type == "president apartment":
    if nights_count < 10:
        discount = 0.9
    elif 10 <= nights_count <= 15:
        discount = 0.85
    else:
        discount = 0.8
    price = nights_count * 35 * discount

if rating == "positive":
    price *= 1.25
else:
    price *= 0.90

print(f"{price:.2f}")
