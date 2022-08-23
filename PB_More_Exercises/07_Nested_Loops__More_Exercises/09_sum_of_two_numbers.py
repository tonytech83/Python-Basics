start = int(input())
end = int(input())
magic_number = int(input())

counter = 0
found_combination = False

for first in range(start, end + 1):
    for second in range(start, end + 1):
        counter += 1
        if first + second == magic_number:
            found_combination = True
            break
    if found_combination:
        break

if found_combination:
    print(f'Combination N:{counter} ({first} + {second} = {magic_number})')
else:
    print(f'{counter} combinations - neither equals {magic_number}')
