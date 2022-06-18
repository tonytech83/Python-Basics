days = int(input())
room_type = input()
rating = input()

overnights = days - 1

total_price = 0

if room_type == "room for one person":
    total_price = overnights * 18.00

elif room_type == "apartment":
    total_price = overnights * 25.00
    if overnights < 10:
        total_price *= 0.7
    elif 10 <= overnights <= 15:
        total_price *= 0.65
    else:
        total_price *= 0.5

else:
    total_price = overnights * 35.00
    if overnights < 10:
        total_price *= 0.9
    elif 10 <= overnights <= 15:
        total_price *= 0.85
    else:
        total_price *= 0.8

if rating == "positive":
    total_price *= 1.25
else:
    total_price *= 0.9

print(f"{total_price:.2f}")
