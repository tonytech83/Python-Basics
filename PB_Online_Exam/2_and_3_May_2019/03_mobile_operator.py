contract_term = input()
contract_type = input()
internet_package = input()
months_to_pay = int(input())

final_price = 0

if contract_term == "one":
    if contract_type == "Small":
        final_price = 9.98 * months_to_pay
    elif contract_type == "Middle":
        final_price = 18.99 * months_to_pay
    elif contract_type == "Large":
        final_price = 25.98 * months_to_pay
    else:  # ExtraLarge
        final_price = 35.99 * months_to_pay

else:
    if contract_type == "Small":
        final_price = 8.58 * months_to_pay
    elif contract_type == "Middle":
        final_price = 17.09 * months_to_pay
    elif contract_type == "Large":
        final_price = 23.59 * months_to_pay
    else:  # ExtraLarge
        final_price = 31.79 * months_to_pay

if internet_package == "yes":
    if final_price / months_to_pay <= 10:
        final_price += 5.5 * months_to_pay
    elif final_price / months_to_pay <= 30:
        final_price += 4.35 * months_to_pay
    else:
        final_price += 3.85 * months_to_pay

if contract_term == "two":
    final_price *= 0.9625

print(f"{final_price:.2f} lv.")
