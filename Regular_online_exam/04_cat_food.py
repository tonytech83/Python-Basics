cats = int(input())

group_1 = 0
group_2 = 0
group_3 = 0

total_meal = 0

for cat in range(cats):
    current_meal = float(input())
    if current_meal < 200:
        group_1 += 1
        total_meal += current_meal
    elif 200 <= current_meal < 300:
        group_2 += 1
        total_meal += current_meal
    else:
        group_3 += 1
        total_meal += current_meal

meal_price = total_meal / 1000 * 12.45

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {meal_price:.2f} lv.")
