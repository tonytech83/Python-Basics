stage = input()
ticket_type = input()
ticket_count = int(input())
picture_with_trophy = input()

tickets_price = 0
total_price = 0

if stage == "Quarter final":
    if ticket_type == "Standard":
        tickets_price = ticket_count * 55.5
    elif ticket_type == "Premium":
        tickets_price = ticket_count * 105.2
    else:
        tickets_price = ticket_count * 118.9
elif stage == "Semi final":
    if ticket_type == "Standard":
        tickets_price = ticket_count * 75.88
    elif ticket_type == "Premium":
        tickets_price = ticket_count * 125.22
    else:
        tickets_price = ticket_count * 300.4
else:
    if ticket_type == "Standard":
        tickets_price = ticket_count * 110.1
    elif ticket_type == "Premium":
        tickets_price = ticket_count * 160.66
    else:
        tickets_price = ticket_count * 400

if tickets_price > 4000:
    total_price = tickets_price * 0.75
elif tickets_price > 2500:
    total_price = tickets_price * 0.9
    if picture_with_trophy == "Y":
        total_price += ticket_count * 40
else:
    total_price = tickets_price
    if picture_with_trophy == "Y":
        total_price += ticket_count * 40

print(f"{total_price:.2f}")
