import math

vineyard_area = int(input())
grapes_per_square = float(input())
required_vine = int(input())
workers_count = int(input())

grapes_produced = vineyard_area * grapes_per_square
grapes_for_vine = grapes_produced * 0.4

produced_vine = grapes_for_vine / 2.5

diff = abs(math.floor(required_vine - produced_vine))

if produced_vine < required_vine:
    print(f'It will be a tough winter! More {diff} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(produced_vine)} liters.')
    vine_per_worker = math.ceil(diff / workers_count)
    print(f'{int(diff)} liters left -> {vine_per_worker} liters per person.')
