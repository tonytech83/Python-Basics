budget = float(input())
ticket_type = input()
fans = int(input())

transport = 0
total_price = 0

if fans <= 4:
    transport = budget * 0.75
elif 4 < fans <= 9:
    transport = budget * 0.6
elif 9 < fans <= 24:
    transport = budget * 0.5
elif 24 < fans <= 49:
    transport = budget * 0.4
else:
    transport = budget * 0.25

if ticket_type == 'VIP':
    total_price = fans * 499.99 + transport
else:
    total_price = fans * 249.99 + transport

diff = abs(budget - total_price)

if budget > total_price:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')
