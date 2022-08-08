customers = int(input())
overall_price = 0

for customer in range(customers):
    purchase = input()
    customer_purchases = 0
    customer_spend = 0
    while purchase != 'Finish':
        customer_purchases += 1
        if purchase == 'basket':
            customer_spend += 1.5

        elif purchase == 'wreath':
            customer_spend += 3.8

        else:
            customer_spend += 7

        purchase = input()

    if customer_purchases % 2 == 0:
        customer_spend *= 0.8

    overall_price += customer_spend

    print(f'You purchased {customer_purchases} items for {customer_spend:.2f} leva.')

average_price = overall_price / customers

print(f'Average bill per client is: {average_price:.2f} leva.')
