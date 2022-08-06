destination = input()
reservation = input()
trip_dates = int(input())

total = 0

if destination == "France":
    if reservation == "21-23":
        total = trip_dates * 30
    elif reservation == "24-27":
        total = trip_dates * 35
    else:
        total = trip_dates * 40
elif destination == "Italy":
    if reservation == "21-23":
        total = trip_dates * 28
    elif reservation == "24-27":
        total = trip_dates * 32
    else:
        total = trip_dates * 39
else:
    if reservation == "21-23":
        total = trip_dates * 32
    elif reservation == "24-27":
        total = trip_dates * 37
    else:
        total = trip_dates * 43

print(f'Easter trip to {destination} : {total:.2f} leva.')