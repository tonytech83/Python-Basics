film_name = input()

student_tickets_count = 0
standard_tickets_count = 0
kid_tickets_count = 0
total_tickets_count_per_film = 0
ticket_type = ""
total_tickets = 0

while film_name != "Finish":
    free_seats = int(input())
    ticket_type = input()
    total_tickets_count_per_film = 0
    while ticket_type != "End":
        free_seats -= 1
        total_tickets_count_per_film += 1
        if ticket_type == "student":
            student_tickets_count += 1
        elif ticket_type == "standard":
            standard_tickets_count += 1
        else:
            kid_tickets_count += 1
        if free_seats == 0:
            break
        ticket_type = input()

    total_tickets += total_tickets_count_per_film

    percent_occupancy_per_film = total_tickets_count_per_film / (total_tickets_count_per_film + free_seats) * 100

    print(f"{film_name} - {percent_occupancy_per_film:.2f}% full.")

    film_name = input()

print(f"Total tickets: {total_tickets}")

percent_student_tickets = student_tickets_count / total_tickets * 100
percent_standard_tickets = standard_tickets_count / total_tickets * 100
percent_kid_tickets = kid_tickets_count / total_tickets * 100

print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")
