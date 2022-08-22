number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

division_count = 0

for num1 in range(2, number_1 + 1):
    for num2 in range(2, number_2 + 1):
        for num3 in range(2, number_3 + 1):
            for division in range(2, num2 + 1):

                if num1 % 2 == 0 and num3 % 2 == 0 and (num2 % division) == 0:
                    division_count += 1

            if division_count >= 2:
                division_count = 0
                continue
            if num1 % 2 == 0 and num3 % 2 == 0:
                print(f'{num1} {num2} {num3}')
                division_count = 0
