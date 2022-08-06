eggs_size = input()
eggs_paint = input()
eggs_count = int(input())

price = 0

if eggs_size == 'Large':
    if eggs_paint == 'Red':
        price = eggs_count * 16
    elif eggs_paint == 'Green':
        price = eggs_count * 12
    else:
        price = eggs_count * 9

elif eggs_size == 'Medium':
    if eggs_paint == 'Red':
        price = eggs_count * 13
    elif eggs_paint == 'Green':
        price = eggs_count * 9
    else:
        price = eggs_count * 7

else:
    if eggs_paint == 'Red':
        price = eggs_count * 9
    elif eggs_paint == 'Green':
        price = eggs_count * 8
    else:
        price = eggs_count * 5

profit = price * 0.65

print(f'{profit:.2f} leva.')
