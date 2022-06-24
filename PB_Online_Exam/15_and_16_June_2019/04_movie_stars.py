budget = float(input())

actor_name = input()

while actor_name != "ACTION":
    if len(actor_name) <= 15:
        payment = float(input())
        budget -= payment
    else:
        budget -= budget * 0.2

    if budget < 0:
        break

    actor_name = input()

if budget > 0:
    print(f"We are left with {abs(budget):.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")
