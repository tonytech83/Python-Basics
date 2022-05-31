target_profit = float(input())

bill = 0
profit = 0

while target_profit >= profit:
    cocktail = input()
    if cocktail == "Party!":
        break
    cocktail_count = int(input())
    bill = len(cocktail) * cocktail_count
    if bill % 2 != 0:
        bill = bill * 0.75
        profit += bill
    else:
        profit += bill

diff = abs(target_profit - profit)

if cocktail == "Party!":
    print(f"We need {diff:.2f} leva more.")
    print(f"Club income - {profit:.2f} leva.")

else:
    print(f"Target acquired.")
    print(f"Club income - {profit:.2f} leva.")

# TODO 90/100