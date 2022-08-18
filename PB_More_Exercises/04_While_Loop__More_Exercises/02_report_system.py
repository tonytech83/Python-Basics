target_money = int(input())

purchase = input()
purchase_count = 0
cash_count = 0
card_count = 0
cash_purchase = 0
card_purchase = 0

while purchase != 'End':

    purchase_count += 1

    if purchase_count % 2 != 0:
        if int(purchase) > 100:
            print('Error in transaction!')
            purchase = input()
            continue

        cash_purchase += int(purchase)
        cash_count += 1
        print('Product sold!')
        target_money -= int(purchase)
    else:
        if int(purchase) < 10:
            print('Error in transaction!')
            purchase = input()
            continue

        card_purchase += int(purchase)
        card_count += 1
        print('Product sold!')
        target_money -= int(purchase)

    if target_money <= 0:
        break

    purchase = input()

if target_money <= 0:
    average_cash = cash_purchase / cash_count
    average_card = card_purchase / card_count
    print(f'Average CS: {average_cash:.2f}')
    print(f'Average CC: {average_card:.2f}')
else:
    print('Failed to collect required money for charity.')
