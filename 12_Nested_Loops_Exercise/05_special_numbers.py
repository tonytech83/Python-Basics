number_input = int(input())

division_count = 0

for special in range(1111, 10000):
    division_count = 0
    special_to_str = str(special)
    for index, digit in enumerate(special_to_str):
        if int(digit) == 0:
            break
        if number_input % int(digit) == 0:
            division_count += 1
        else:
            break
    if division_count == 4:
        print(special, end=" ")
