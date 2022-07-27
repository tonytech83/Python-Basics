from math import floor

tournament_count = int(input())
starting_points = int(input())

win_points = 0
wins = 0

for tournament in range(tournament_count):
    tournament_stage = input()
    if tournament_stage == "W":
        wins += 1
        current_points = 2000
    elif tournament_stage == "F":
        current_points = 1200
    else:
        current_points = 720

    win_points += current_points

final_points = starting_points + win_points
average_points = floor(win_points / tournament_count)
percent_wins = wins / tournament_count * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percent_wins:.2f}%")
