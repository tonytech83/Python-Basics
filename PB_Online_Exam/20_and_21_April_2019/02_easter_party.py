guests_count = int(input())
price_per_person = float(input())
budget = float(input())

cake_price = budget * 0.1

if 10 <= guests_count <= 15:
    price_per_person *= 0.85

elif 15 < guests_count <= 20:
    price_per_person *= 0.8

elif guests_count > 20:
    price_per_person *= 0.75

if budget > guests_count * price_per_person + cake_price:
    left_money = budget - guests_count * price_per_person - cake_price
    print(f'It is party time! {left_money:.2f} leva left.')
else:
    needed_money = guests_count * price_per_person + cake_price - budget
    print(f'No party! {needed_money:.2f} leva needed.')
