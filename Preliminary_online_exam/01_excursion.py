group_count = int(input())
overnight_count = int(input())
transport_card_count = int(input())
museum_tickets_count = int(input())

overnight_total = overnight_count * 20
transport_card_total = transport_card_count * 1.6
museum_tickets_total = museum_tickets_count * 6

price_per_person = overnight_total + transport_card_total + museum_tickets_total
price_for_group = price_per_person * group_count

final_price = price_for_group * 1.25

print(f"{final_price:.2f}")
