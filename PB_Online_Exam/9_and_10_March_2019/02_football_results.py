team_won = 0
team_lost = 0
team_drawn = 0

for game in range(3):
    current_game = input()
    if current_game[0] > current_game[2]:
        team_won += 1
    elif current_game[0] < current_game[2]:
        team_lost += 1
    elif current_game[0] == current_game[2]:
        team_drawn += 1

print(f"Team won {team_won} games.")
print(f"Team lost {team_lost} games.")
print(f"Drawn games: {team_drawn}")
