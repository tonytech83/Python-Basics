bought_food = int(input()) * 1000
total_food = 0
food_per_day = input()


while food_per_day != "Adopted":
    total_food += int(food_per_day)
    food_per_day = input()

diff = abs(bought_food - total_food)

if total_food <= bought_food:
    print(f'Food is enough! Leftovers: {diff} grams.')
else:
    print(f'Food is not enough. You need {diff} grams more.')