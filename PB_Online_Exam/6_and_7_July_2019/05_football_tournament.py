football_team = input()
game_count = int(input())

total_points = 0
wins = 0
draws = 0
losses = 0

percent_wins = 0
special_message = True

for game in range(game_count):
    special_message = False
    current_result = input()
    if current_result == "W":
        wins += 1
        total_points += 3
    elif current_result == "D":
        draws += 1
        total_points += 1
    else:
        losses += 1

if special_message:
    print(f"{football_team} hasn't played any games during this season.")

else:
    win_rate = wins / game_count * 100

    print(f"{football_team} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {losses}")
    print(f"Win rate: {win_rate:.2f}%")
