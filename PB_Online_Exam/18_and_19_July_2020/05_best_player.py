player_name = input()

scorer = None
is_do_hat_trick = False
most_goals = 0

while player_name != "END":

    scored_goals = int(input())

    if scored_goals > most_goals:
        scorer = player_name
        most_goals = scored_goals

    if 3 <= scored_goals < 10:
        is_do_hat_trick = True

    if scored_goals >= 10:
        is_do_hat_trick = True
        break

    player_name = input()

print(f'{scorer} is the best player!')

if is_do_hat_trick:
    print(f'He has scored {most_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {most_goals} goals.')
