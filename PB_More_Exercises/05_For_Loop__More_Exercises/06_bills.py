period = int(input())

electricity = 0
water = 20 * period
internet = 15 * period
other = 0


for month in range(period):
    electricity_bill = float(input())
    electricity += electricity_bill
    other += (electricity_bill + 20 + 15) * 1.2

total = electricity + water + internet + other

average_per_month = total / period

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average_per_month:.2f} lv')


