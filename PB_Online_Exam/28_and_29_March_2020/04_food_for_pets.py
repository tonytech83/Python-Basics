days = int(input())
total_food = float(input())

dog_eaten = 0
cat_eaten = 0
total_biscuits = 0
total_eaten = 0

for day in range(1, days + 1):
    dog = int(input())
    cat = int(input())

    dog_eaten += dog
    cat_eaten += cat
    total_eaten = dog_eaten + cat_eaten

    if day % 3 == 0:
        biscuits = (dog + cat) * 0.1
        total_biscuits += biscuits

percent_eaten_food = total_eaten / total_food * 100
percent_dog = dog_eaten / total_eaten * 100
percent_cat = cat_eaten / total_eaten * 100

print(f'Total eaten biscuits: {round(total_biscuits)}gr.')
print(f'{percent_eaten_food:.2f}% of the food has been eaten.')
print(f'{percent_dog:.2f}% eaten from the dog.')
print(f'{percent_cat:.2f}% eaten from the cat.')
