hall_rent = int(input())

statuette_price = hall_rent * 0.7
catering_price = statuette_price * 0.85
sound_price = catering_price / 2

total_spend = hall_rent + statuette_price + catering_price + sound_price

print(f"{total_spend:.2f}")
