hall_capacity = int(input())

people_entered = 0
income_money = 0

incoming_people = input()

while incoming_people != "Movie time!":
    incoming_people = int(incoming_people)
    people_entered += incoming_people

    if people_entered > hall_capacity:
        break

    if incoming_people % 3 == 0:
        income_money += (incoming_people * 5) - 5
    else:
        income_money += incoming_people * 5

    incoming_people = input()

left_seats = abs(hall_capacity - people_entered)

if people_entered > hall_capacity:
    print(f"The cinema is full.")
else:
    print(f"There are {left_seats} seats left in the cinema.")

print(f"Cinema income - {income_money} lv.")
