from math import floor, ceil

leave_days = int(input())
food_in_kg = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) / 1000

needed_food = (dog_food + cat_food + turtle_food) * leave_days

diff = abs(food_in_kg - needed_food)

if food_in_kg >= needed_food:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')
