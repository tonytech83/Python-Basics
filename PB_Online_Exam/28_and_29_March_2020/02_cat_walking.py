minutes_walk = int(input())
walks_per_day = int(input())
calories_per_day = int(input())

burned_calories = walks_per_day * minutes_walk * 5

if burned_calories >= calories_per_day * 0.5:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.')
