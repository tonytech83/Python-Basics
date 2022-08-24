days = int(input())
hours = int(input())

day_tax = 0
total = 0

for day in range(1, days + 1):
    for hour in range(1, hours + 1):

        if day % 2 == 0 and hour % 2 != 0:
            day_tax += 2.5

        elif day % 2 != 0 and hour % 2 == 0:
            day_tax += 1.25

        else:
            day_tax += 1

    total += day_tax
    print(f'Day: {day} - {day_tax:.2f} leva')
    day_tax = 0
print(f'Total: {total:.2f} leva')
