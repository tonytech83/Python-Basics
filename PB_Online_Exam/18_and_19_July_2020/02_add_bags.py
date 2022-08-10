baggage_price = float(input())
baggage_kg = float(input())
days_until_trip = int(input())
baggage_count = int(input())

if baggage_kg < 10:
    baggage_price *= 0.2
elif 10 <= baggage_kg <= 20:
    baggage_price *= 0.5

if days_until_trip > 30:
    baggage_price *= 1.1
elif 30 >= days_until_trip >= 7:
    baggage_price *= 1.15
else:
    baggage_price *= 1.4

total = baggage_count * baggage_price

print(f'The total price of bags is: {total:.2f} lv.')