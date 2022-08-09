btc = int(input())
cny = float(input())
commission = float(input())

btc_to_eur = btc * 1168 / 1.95
cny_to_eur = cny * 0.15 * 1.76 / 1.95

total_eur = (btc_to_eur + cny_to_eur) - (btc_to_eur + cny_to_eur) * commission / 100

print(f'{total_eur:.2f}')
