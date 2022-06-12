destination = input()

saved = 0
is_going = False

while destination != "End":
    saved = 0
    needed_budget = float(input())
    while needed_budget > saved:
        input_money = float(input())
        saved += input_money

    print(f"Going to {destination}!")

    destination = input()
