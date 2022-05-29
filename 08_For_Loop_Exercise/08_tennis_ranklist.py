tournament_count = int(input())
starting_points = int(input())

earned_points = 0
wins = 0

for game in range(tournament_count):
    status_of_game = input()
    if status_of_game == "W":
        earned_points += 2000
        wins += 1
    elif status_of_game == "F":
        earned_points += 1200
    else:
        earned_points += 720

total_points = starting_points + earned_points
average_earned_points = int(earned_points / tournament_count)
wined_tournaments = wins / tournament_count * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_earned_points}")
print(f"{wined_tournaments:.2f}%")
