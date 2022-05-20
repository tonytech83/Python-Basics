nylon = int(input())
paint = int(input())
paint_thinner = int(input())
workers_hours = int(input())

price_nylon = (nylon + 2) * 1.50
price_paint = (paint + paint * 0.1) * 14.50
price_thinner = paint_thinner * 5.00

total_materials = price_nylon + price_paint + price_thinner + 0.40
total_workers = total_materials * 0.3 * workers_hours

result = total_materials + total_workers

print(result)
