from math import ceil

people_count = int(input())
entrance_fee = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

total_in_fees = people_count * entrance_fee
total_umbrella_fees = ceil(people_count / 2) * umbrella_price
total_sunbed_fees = ceil(people_count * 0.75) * sunbed_price

total_price = total_in_fees + total_umbrella_fees + total_sunbed_fees

print(f"{total_price:.2f} lv.")
