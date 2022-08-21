n = int(input())

stars = 1
dash = (n - stars) // 2
mid = 0

if n % 2 == 0:
    rows = n // 2
    stars = 2
    for row in range(rows):
        print('-' * dash + '*' * (stars // 2) + '-' * mid + '*' * (stars // 2) + '-' * dash)
        dash -= 1
        mid += 2

    dash = 0
    mid -= 2
    for row in range((n - rows) - 1):
        mid -= 2
        dash += 1
        print('-' * dash + '*' * (stars // 2) + '-' * mid + '*' * (stars // 2) + '-' * dash)
else:
    rows = n // 2
    print('-' * dash + '*' * stars + '-' * dash)
    mid = 1
    for row in range(rows):
        dash -= 1
        print('-' * dash + '*' * stars + '-' * mid + '*' * stars + '-' * dash)
        mid += 2
    mid = n - 4
    for row in range((n - rows) - 2):
        dash += 1
        print('-' * dash + '*' * stars + '-' * mid + '*' * stars + '-' * dash)
        mid -= 2
    if n > 1:
        print('-' * (dash + 1) + '*' * stars + '-' * (dash + 1))
