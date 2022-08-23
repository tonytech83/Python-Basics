hundreds = int(input())
tens = int(input())
units = int(input())

division_count = 0

for first in range(2, hundreds + 1):
    for second in range(2, tens + 1):
        for third in range(2, units + 1):
            for division in range(2, second + 1):
                if first % 2 == 0 and third % 2 == 0 and (second % division) == 0:
                    division_count += 1

            if division_count >= 2:
                division_count = 0
                continue
            if first % 2 == 0 and third % 2 == 0:
                print(f'{first} {second} {third}')
                division_count = 0
