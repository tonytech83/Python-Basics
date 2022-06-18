best_player = ""
made_hat_trick = False
most_goals = 0

current_player = input()

while current_player != "END":

    current_goals = int(input())
    if current_goals > most_goals:
        most_goals = current_goals
        best_player = current_player
        if 2 < current_goals < 10:
            made_hat_trick = True
        elif current_goals >= 10:
            made_hat_trick = True
            break
    current_player = input()

print(f"{best_player} is the best player!")
if made_hat_trick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")
