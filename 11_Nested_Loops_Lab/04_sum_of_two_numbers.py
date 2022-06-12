start_number = int(input())
end_number = int(input())
magic_number = int(input())

count = 0
found_it = False

for number1 in range(start_number, end_number + 1):
    for number2 in range(start_number, end_number + 1):
        count += 1
        if number1 + number2 == magic_number:
            found_it = True
            break
    if found_it:
        break

if found_it:
    print(f"Combination N:{count} ({number1} + {number2} = {magic_number})")
else:
    print(f"{count} combinations - neither equals {magic_number}")