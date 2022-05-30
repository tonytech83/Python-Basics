drink_type = input()
sugar = input()
drink_count = int(input())

final_price = 0

if sugar == "Without":
    if drink_type == "Espresso":
        final_price = (drink_count * 0.9) * 0.65
        if drink_count >= 5:
            final_price = final_price * 0.75
    elif drink_type == "Cappuccino":
        final_price = drink_count * 1 * 0.65
    else:
        final_price = drink_count * 0.5 * 0.65
elif sugar == "Normal":
    if drink_type == "Espresso":
        final_price = drink_count * 1
        if drink_count >= 5:
            final_price = final_price * 0.75
    elif drink_type == "Cappuccino":
        final_price = drink_count * 1.2
    else:
        final_price = drink_count * 0.6
else:
    if drink_type == "Espresso":
        final_price = drink_count * 1.2
        if drink_count >= 5:
            final_price = final_price * 0.75
    elif drink_type == "Cappuccino":
        final_price = drink_count * 1.6
    else:
        final_price = drink_count * 0.7

if final_price > 15:
    final_price = final_price * 0.8

print(f"You bought {drink_count} cups of {drink_type} for {final_price:.2f} lv.")
