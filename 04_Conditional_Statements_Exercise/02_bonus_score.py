def bonus_points(points):
    if points <= 100:
        bonus = 5

    elif 100 < points <= 1000:
        bonus = points * 0.2

    elif points > 1000:
        bonus = points * 0.1

    if points % 2 == 0:
        bonus += 1

    elif points % 5 == 0:
        bonus += 2

    total = points + bonus
    print(f"{bonus}")
    print(f"{total}")


initial_points = int(input())

bonus_points(initial_points)
