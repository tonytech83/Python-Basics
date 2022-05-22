budget = int(input())
season = input()
fishermen_count = int(input())

boat_rent = 0
final_price = 0

# check the rent season to determine the price
if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
else:  # check for Winter
    boat_rent = 2600

# check the fisherman count to determine the discount
if fishermen_count <= 6:
    final_price = boat_rent * 0.9
elif 7 <= fishermen_count <= 11:
    final_price = boat_rent * 0.85
else:  # check when fishermen are more than 11
    final_price = boat_rent * 0.75

# check if fishermen are even
if fishermen_count % 2 == 0 and season != "Autumn":
    final_price *= 0.95

diff = abs(budget - final_price)

if budget >= final_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
