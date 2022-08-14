from math import ceil

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

profit_before_tax = magnolias_count * 3.25 + hyacinths_count * 4 + roses_count * 3.5 + cactus_count * 8
profit_after_tax = profit_before_tax * 0.95

diff = abs(profit_after_tax - gift_price)

if gift_price <= profit_after_tax:
    print(f'She is left with {int(diff)} leva.')
else:
    print(f'She will have to borrow {ceil(diff)} leva.')
