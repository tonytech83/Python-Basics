n = int(input())
trip_time = input()

if n < 20:
    if trip_time == 'day':
        price = 0.7 + 0.79 * n
    else:
        price = 0.7 + 0.9 * n
elif 20 <= n < 100:
    price = 0.09 * n
else:
    price = 0.06 * n

print(f'{price:.2f}')
