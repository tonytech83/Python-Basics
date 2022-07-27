player_one = input()
player_two = input()

player_one_points = 0
player_two_points = 0
is_number_wars = False

player_one_turn = input()

while player_one_turn != "End of game":
    player_one_turn = int(player_one_turn)
    player_two_turn = int(input())
    if player_one_turn > player_two_turn:
        player_one_points += player_one_turn - player_two_turn
    elif player_one_turn < player_two_turn:
        player_two_points += player_two_turn - player_one_turn
    else:
        player_one_turn = int(input())
        player_two_turn = int(input())
        if player_one_turn > player_two_turn:
            winner = player_one
            winner_points = player_one_points
            is_number_wars = True
            break
        elif player_one_turn < player_two_turn:
            winner_points = player_two_points
            winner = player_two
            is_number_wars = True
            break

    player_one_turn = input()

if is_number_wars:
    print('Number wars!')
    print(f'{winner} is winner with {winner_points} points')
else:
    print(f'{player_one} has {player_one_points} points')
    print(f'{player_two} has {player_two_points} points')
