number = int(input())

number_to_string = str(number)

first_digit = int(number_to_string[2])
second_digit = int(number_to_string[1])
third_digit = int(number_to_string[0])

for first in range(1, first_digit + 1):
    for second in range(1, second_digit + 1):
        for third in range(1, third_digit + 1):
            result = first * second * third
            print(f"{first} * {second} * {third} = {result};")
