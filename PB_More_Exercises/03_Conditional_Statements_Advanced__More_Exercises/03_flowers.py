chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
holiday = input()

total_flowers = chrysanthemums_count + roses_count + tulips_count
total_price = 0

if season == 'Spring' or season == 'Summer':
    total_price = chrysanthemums_count * 2 + roses_count * 4.1 + tulips_count * 2.5
    if tulips_count > 7 and season == 'Spring':
        total_price *= 0.95
    if total_flowers > 20:
        total_price *= 0.8
else:
    total_price = chrysanthemums_count * 3.75 + roses_count * 4.5 + tulips_count * 4.15
    if roses_count >= 10 and season == 'Winter':
        total_price *= 0.9
    if total_flowers > 20:
        total_price *= 0.8

if holiday == 'Y':
    total_price *= 1.15

total_price += 2

print(f'{total_price:.2f}')
