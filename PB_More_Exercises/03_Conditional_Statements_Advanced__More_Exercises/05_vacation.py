budget = float(input())
season = input()

price = 0

if budget <= 1000:
    place = 'Camp'
    if season == 'Summer':
        destination = 'Alaska'
        price = budget * 0.65
    else:
        price = budget * 0.45
        destination = 'Morocco'
elif 1000 < budget <= 3000:
    place = 'Hut'
    if season == 'Summer':
        price = budget * 0.8
        destination = 'Alaska'
    else:
        price = budget * 0.6
        destination = 'Morocco'
else:
    place = 'Hotel'
    if season == 'Summer':
        destination = 'Alaska'
    else:
        destination = 'Morocco'
    price = budget * 0.9

print(f'{destination} - {place} - {price:.2f}')
