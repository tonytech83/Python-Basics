from math import floor, ceil

tennis_racket_price = float(input())
tennis_racket_count = int(input())
sneakers_count = int(input())

sneakers_price = tennis_racket_price / 6

price_before_others = tennis_racket_count * tennis_racket_price + sneakers_count * sneakers_price

others_price = price_before_others * 0.2

final_price = price_before_others + others_price

print(f"Price to be paid by Djokovic {floor(final_price / 8)}")
print(f"Price to be paid by sponsors {ceil(final_price * 7 / 8)}")
