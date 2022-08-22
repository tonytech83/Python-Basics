last_sector = input()
rows_count = int(input())
seats_count = int(input())

memory = seats_count
counter = 0

last_sector_str = ord(last_sector)

for sector in range(65, last_sector_str + 1):
    for row in range(1, rows_count + 1):
        if row % 2 == 0:
            seats_count += 2
        for seat in range(97, (97 + seats_count)):
            counter += 1

            print(f'{chr(sector)}{row}{chr(seat)}')

        if seats_count == memory + 2:
            seats_count -= 2
    rows_count += 1

print(counter)
