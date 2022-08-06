price_flour_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_count = int(input())
yeast_count = int(input())

price_sugar_kg = price_flour_kg * 0.75
price_eggs = price_flour_kg * 1.1
price_yeast = price_sugar_kg * 0.2

total_flour = price_flour_kg * flour_kg
total_sugar = price_sugar_kg * sugar_kg
total_eggs = price_eggs * eggs_count
total_yeast = price_yeast * yeast_count

total = total_flour + total_sugar + total_eggs + total_yeast

print(f'{total:.2f}')
