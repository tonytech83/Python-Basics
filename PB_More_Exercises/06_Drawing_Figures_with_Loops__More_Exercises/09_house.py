n = int(input())

stars = 1
dash = (n - stars) // 2

if n % 2 == 0:
    rows = n // 2
    stars = 2
else:
    rows = n // 2 + 1

for row in range(int(rows)):
    print("-" * dash + "*" * stars + "-" * dash)
    stars += 2
    dash = (n - stars) // 2

for row in range(n - rows):
    print("|" + "*" * (n - 2) + "|")
