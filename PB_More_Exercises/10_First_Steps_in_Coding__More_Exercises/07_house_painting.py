x = float(input())
y = float(input())
h = float(input())

door = 1.2 * 2
window = 1.5 * 1.5

green_parts = x * x * 2 + y * x * 2 - door - window * 2
green_paint = green_parts / 3.4

red_parts = (x * h / 2) * 2 + x * y * 2
red_paint = red_parts / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
