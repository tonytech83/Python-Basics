work_season = input()
km_per_month = float(input())

profit = 0

if km_per_month <= 5000:
    if work_season == 'Spring' or work_season == 'Autumn':
        profit = 4 * km_per_month * 0.75
    elif work_season == 'Summer':
        profit = 4 * km_per_month * 0.9
    else:
        profit = 4 * km_per_month * 1.05
elif 5000 < km_per_month <= 10000:
    if work_season == 'Spring' or work_season == 'Autumn':
        profit = 4 * km_per_month * 0.95
    elif work_season == 'Summer':
        profit = 4 * km_per_month * 1.1
    else:
        profit = 4 * km_per_month * 1.25
elif 10000 < km_per_month <= 20000:
    profit = 4 * km_per_month * 1.45

profit *= 0.9

print(f'{profit:.2f}')
