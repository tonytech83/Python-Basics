mackerel_price = float(input())
sprinkle_price = float(input())

bonito_quantity = float(input())
safrid_quantity = float(input())
mussels_quantity = int(input())

bonito_price = mackerel_price * 1.6
safrid_price = sprinkle_price * 1.8
mussels_price = 7.5

total = bonito_quantity * bonito_price + safrid_quantity * safrid_price + mussels_quantity * mussels_price

print(f'{total:.2f}')
