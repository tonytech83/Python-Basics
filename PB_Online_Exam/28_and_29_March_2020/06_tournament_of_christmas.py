tournament_days = int(input())

total_wins = 0
total_loses = 0
total_earned_money = 0

for tournament in range(tournament_days):

    sport = input()
    wins = 0
    loses = 0
    earned_money = 0

    while sport != 'Finish':
        result = input()
        if result == 'win':
            earned_money += 20
            wins += 1
        else:
            loses += 1

        sport = input()

    if wins > loses:
        earned_money *= 1.1

    total_wins += wins
    total_loses += loses

    total_earned_money += earned_money

if total_wins > total_loses:
    total_earned_money *= 1.2
    print(f'You won the tournament! Total raised money: {total_earned_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_earned_money:.2f}')
