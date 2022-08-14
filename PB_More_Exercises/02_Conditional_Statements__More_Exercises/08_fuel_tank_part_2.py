fuel_type = input()
fuel_amount = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

final_price = 0

if fuel_type == 'Gas':
    if club_card == 'Yes':
        gas_price -= 0.08

    final_price = fuel_amount * gas_price

elif fuel_type == 'Gasoline':
    if club_card == "Yes":
        gasoline_price -= 0.18

    final_price = fuel_amount * gasoline_price

else:
    if club_card == "Yes":
        diesel_price -= 0.12

    final_price = fuel_amount * diesel_price

if 20 <= fuel_amount <= 25:
    final_price *= 0.92
elif fuel_amount > 25:
    final_price *= 0.9

print(f'{final_price:.2f} lv.')
