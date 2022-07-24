def equipment_calc(training_fee):
    sneakers_price = training_fee * 0.6
    outfit_price = sneakers_price * 0.8
    ball_price = outfit_price / 4
    accessors_price = ball_price / 5
    total = training_fee + sneakers_price + outfit_price + ball_price + accessors_price
    return total


training_fee = int(input())

final_price = equipment_calc(training_fee)

print(f"{final_price:.2f}")
