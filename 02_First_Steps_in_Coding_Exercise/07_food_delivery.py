chicken_nemu = int(input())
fish_nemu = int(input())
vegan_nemu = int(input())

price_chicken = chicken_nemu * 10.35
price_fish = fish_nemu * 12.40
price_vegan = vegan_nemu * 8.15

total_menu_price = price_vegan + price_fish + price_chicken
dessert_price = total_menu_price * 0.20

final_price = total_menu_price + dessert_price + 2.50

print(final_price)

