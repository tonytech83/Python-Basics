budget = float(input())
sex = input()
age = int(input())
activity = input()

price = 0

if sex == 'm':
    if activity == 'Gym':
        price = 42
    elif activity == 'Boxing':
        price = 41
    elif activity == 'Yoga':
        price = 45
    elif activity == 'Zumba':
        price = 34
    elif activity == 'Dances':
        price = 51
    else:
        price = 39

else:
    if activity == 'Gym':
        price = 35
    elif activity == 'Boxing':
        price = 37
    elif activity == 'Yoga':
        price = 42
    elif activity == 'Zumba':
        price = 31
    elif activity == 'Dances':
        price = 53
    else:
        price = 37

if age <= 19:
    price *= 0.8

if price <= budget:
    print(f'You purchased a 1 month pass for {activity}.')
else:
    diff = price - budget
    print(f"You don't have enough money! You need ${diff:.2f} more.")

