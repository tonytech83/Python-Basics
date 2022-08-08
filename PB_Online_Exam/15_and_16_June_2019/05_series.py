budget = float(input())
series_count = int(input())

total = 0

for series in range(series_count):
    series_name = input()
    series_price = float(input())

    if series_name == "Thrones":
        total += series_price * 0.5
    elif series_name == "Lucifer":
        total += series_price * 0.6
    elif series_name == "Protector":
        total += series_price * 0.7
    elif series_name == "TotalDrama":
        total += series_price * 0.8
    elif series_name == "Area":
        total += series_price * 0.9
    else:
        total += series_price

diff = abs(budget - total)

if total <= budget:
    print(f'You bought all the series and left with {diff:.2f} lv.')
else:
    print(f'You need {diff:.2f} lv. more to buy the series!')
