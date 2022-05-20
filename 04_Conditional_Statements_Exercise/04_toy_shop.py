def final_profit(trip, puzzle, doll, bear, minion, truck):
    count = puzzle + doll + bear + minion + truck
    total = puzzle * 2.6 + doll * 3 + bear * 4.1 + minion * 8.2 + truck * 2
    if count >= 50:
        profit = total - total * 0.25
    else:
        profit = total
    profit = profit - profit * 0.1
    diff = abs(profit - trip)
    if profit >= trip:
        print(f"Yes! {diff:.2f} lv left.")
    else:
        print(f"Not enough money! {diff:.2f} lv needed.")


trip = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

final_profit(trip, puzzle, doll, bear, minion, truck)
