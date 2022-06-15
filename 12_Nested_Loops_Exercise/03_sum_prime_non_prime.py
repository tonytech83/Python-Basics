input_number = input()

sum_prime = 0
sum_non_prime = 0

while input_number != "stop":
    input_number = int(input_number)
    division_count = 0
    if input_number < 0:
        print("Number is negative.")
        input_number = input()
        continue
    for division in range(1, input_number + 1):

        if input_number % division == 0:
            division_count += 1
        else:
            continue

    if division_count > 2:
        sum_non_prime += input_number
    else:
        sum_prime += input_number

    input_number = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
