tournament_name = input()

total_games = 0
wins = 0
losses = 0

while tournament_name != "End of tournaments":
    games_count = int(input())
    total_games += games_count
    current_game = 0
    for game in range(games_count):
        current_game += 1
        team_one_points = int(input())
        team_two_points = int(input())

        if team_one_points > team_two_points:
            wins += 1
            diff = team_one_points - team_two_points
            print(f'Game {current_game} of tournament {tournament_name}: win with {diff} points.')
        else:
            losses += 1
            diff = team_two_points - team_one_points
            print(f'Game {current_game} of tournament {tournament_name}: lost with {diff} points.')

    tournament_name = input()

percent_wins = wins / total_games * 100
percent_losses = losses / total_games * 100

print(f'{percent_wins:.2f}% matches win')
print(f'{percent_losses:.2f}% matches lost')
