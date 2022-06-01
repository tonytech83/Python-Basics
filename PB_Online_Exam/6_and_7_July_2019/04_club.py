target_profit = float(input())

bill = 0
profit = 0
cocktail = ""

while target_profit > profit:
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

diff = target_profit - profit

if diff > 0 and cocktail == "Party!":
    print(f"We need {diff:.2f} leva more.")
    print(f"Club income - {profit:.2f} leva.")
elif diff <= 0:
    print(f"Target acquired.")
    print(f"Club income - {profit:.2f} leva.")
