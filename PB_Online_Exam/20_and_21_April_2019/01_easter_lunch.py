def price_calc(easter_bread_count, eggs_count, cookie_in_kg, paint_per_egg):
    easter_bread_price = easter_bread_count * 3.2
    eggs_price = eggs_count * 4.35
    cookie_price = cookie_in_kg * 5.40
    eggs = eggs_count * 12
    paint_price = eggs * paint_per_egg
    final_price = easter_bread_price + eggs_price + paint_price + cookie_price
    return final_price


easter_bread_count = int(input())
eggs_count = int(input())
cookie_in_kg = int(input())
paint_per_egg = 0.15

final_price = price_calc(easter_bread_count, eggs_count, cookie_in_kg, paint_per_egg)

print(f"{final_price:.2f}")
