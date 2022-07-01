parking_days = int(input())
hours_each_day = int(input())

day_fee = 0

parking_fee = 0

for day in range(1, parking_days + 1):
    day_fee = 0
    for hour in range(1, hours_each_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            day_fee += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            day_fee += 1.25
        else:
            day_fee += 1

    parking_fee += day_fee

    print(f"Day: {day} - {day_fee:.2f} leva")

print(f"Total: {parking_fee:.2f} leva")
