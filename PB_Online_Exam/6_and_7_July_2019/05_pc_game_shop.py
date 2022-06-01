sold_games = int(input())

game_1 = 0
game_2 = 0
game_3 = 0
game_4 = 0

for game in range(sold_games):
    current_game = input()
    if current_game == "Hearthstone":
        game_1 += 1
    elif current_game == "Fornite":
        game_2 += 1
    elif current_game == "Overwatch":
        game_3 += 1
    else:
        game_4 += 1

print(f"Hearthstone - {(game_1 / sold_games * 100):.2f}%")
print(f"Fornite - {(game_2 / sold_games * 100):.2f}%")
print(f"Overwatch - {(game_3 / sold_games * 100):.2f}%")
print(f"Others - {(game_4 / sold_games * 100):.2f}%")
