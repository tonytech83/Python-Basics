player_name = input()

shot_type = input()

starting_points = 301
scored_points = 0
successful_shots = 0
unsuccessful_shots = 0
left_points = 0

while shot_type != "Retire":
    points = int(input())
    if shot_type == "Triple":
        points *= 3
    elif shot_type == "Double":
        points *= 2

    scored_points += points
    left_points = starting_points - scored_points
    successful_shots += 1

    if left_points == 0:
        break

    if left_points < 0:
        scored_points -= points
        left_points += points
        successful_shots -= 1
        unsuccessful_shots += 1

    shot_type = input()

if shot_type == "Retire":
    print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')
else:
    print(f'{player_name} won the leg with {successful_shots} shots.')
