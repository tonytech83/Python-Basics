detergent_count = int(input())

detergent_amount = 750 * detergent_count

cleaned_dishes = 0
cleaned_pots = 0
counter = 0

dishes = input()

while dishes != "End":
    counter += 1

    if counter % 3 != 0:
        detergent_amount -= int(dishes) * 5
        cleaned_dishes += int(dishes)
    else:
        detergent_amount -= int(dishes) * 15
        cleaned_pots += int(dishes)

    if detergent_amount < 0:
        break

    dishes = input()

if detergent_amount >= 0:
    print('Detergent was enough!')
    print(f'{cleaned_dishes} dishes and {cleaned_pots} pots were washed.')
    print(f'Leftover detergent {detergent_amount} ml.')
else:
    print(f'Not enough detergent, {abs(detergent_amount)} ml. more necessary!')
