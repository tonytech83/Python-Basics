stadium_capacity = int(input())
fans_count = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for fan in range(fans_count):
    sector = input()

    if sector == 'A':
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    else:
        sector_g += 1

percent_sector_a = sector_a / fans_count * 100
percent_sector_b = sector_b / fans_count * 100
percent_sector_v = sector_v / fans_count * 100
percent_sector_g = sector_g / fans_count * 100

percent_per_capacity = fans_count / stadium_capacity * 100

print(f'{percent_sector_a:.2f}%')
print(f'{percent_sector_b:.2f}%')
print(f'{percent_sector_v:.2f}%')
print(f'{percent_sector_g:.2f}%')
print(f'{percent_per_capacity:.2f}%')
