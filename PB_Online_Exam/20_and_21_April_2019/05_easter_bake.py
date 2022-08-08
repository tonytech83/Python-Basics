from math import ceil

bake_count = int(input())

total_sugar = 0
max_sugar = 0
max_flour = 0
total_flour = 0
bigger_bake = 0


for bake in range(bake_count):

    sugar = int(input())
    flour = int(input())

    total_sugar += sugar
    total_flour += flour

    if sugar > max_sugar:
        max_sugar = sugar

    if flour > max_flour:
        max_flour = flour

sugar_package = ceil(total_sugar / 950)
flour_package = ceil(total_flour / 750)

print(f'Sugar: {sugar_package}')
print(f'Flour: {flour_package}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')


