import math

radius = float(input())

circle_area = math.pi * pow(radius, 2)
circle_perimeter = 2 * math.pi * radius

print(f'{circle_area:.2f}')
print(f'{circle_perimeter:.2f}')
