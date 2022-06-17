film_name = input()
hall_type = input()
ticket_count = int(input())

income = 0

if film_name == "A Star Is Born":
    if hall_type == "normal":
        income = ticket_count * 7.5
    elif hall_type == "luxury":
        income = ticket_count * 10.5
    else:
        income = ticket_count * 13.5

elif film_name == "Bohemian Rhapsody":
    if hall_type == "normal":
        income = ticket_count * 7.35
    elif hall_type == "luxury":
        income = ticket_count * 9.45
    else:
        income = ticket_count * 12.75

elif film_name == "Green Book":
    if hall_type == "normal":
        income = ticket_count * 8.15
    elif hall_type == "luxury":
        income = ticket_count * 10.25
    else:
        income = ticket_count * 13.25

else:
    if hall_type == "normal":
        income = ticket_count * 8.75
    elif hall_type == "luxury":
        income = ticket_count * 11.55
    else:
        income = ticket_count * 13.95

print(f"{film_name} -> {income:.2f} lv.")
