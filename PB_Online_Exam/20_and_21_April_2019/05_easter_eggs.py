painted_eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0
max_number = 0

for egg in range(painted_eggs):

    current_egg = input()

    if current_egg == 'red':
        red += 1
    elif current_egg == 'orange':
        orange += 1
    elif current_egg == 'blue':
        blue += 1
    else:
        green += 1

max_number = max(red, orange, blue, green)

print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')

if max_number == red:
    max_paint = 'red'
elif max_number == blue:
    max_paint = 'blue'
elif max_number == orange:
    max_paint = 'orange'
else:
    max_paint = 'green'
print(f'Max eggs: {max_number} -> {max_paint}')
