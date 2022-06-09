tour_budget = float(input())
available_money = float(input())

spend_count = 0
cant_save_money = False
days_count = 0

while available_money < tour_budget:
    action_type = input()
    current_money = float(input())
    days_count += 1
    if action_type == "spend":
        spend_count += 1
        available_money -= current_money
        if available_money < 0:
            available_money = 0
        if spend_count == 5:
            cant_save_money = True
            break
    elif action_type == "save":
        available_money += current_money
        spend_count = 0

if cant_save_money:
    print("You can't save the money.")
    print(f"{days_count}")
else:
    print(f"You saved the money for {days_count} days.")
