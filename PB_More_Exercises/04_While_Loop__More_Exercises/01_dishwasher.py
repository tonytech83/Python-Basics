detergent_count = int(input())

detergent_amount = 750 * detergent_count

cleaned_dishes = 0
cleaned_pots = 0
counter = 0

kitchen_utensils = input()

while kitchen_utensils != "End":
    counter += 1

    if counter % 3 != 0:
        detergent_amount -= int(kitchen_utensils) * 5
        cleaned_dishes += int(kitchen_utensils)
    else:
        detergent_amount -= int(kitchen_utensils) * 15
        cleaned_pots += int(kitchen_utensils)

    if detergent_amount < 0:
        break

    kitchen_utensils = input()

if detergent_amount >= 0:
    print('Detergent was enough!')
    print(f'{cleaned_dishes} dishes and {cleaned_pots} pots were washed.')
    print(f'Leftover detergent {detergent_amount} ml.')
else:
    print(f'Not enough detergent, {abs(detergent_amount)} ml. more necessary!')
