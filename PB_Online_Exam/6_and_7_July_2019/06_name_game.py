# import sys
#
# score = -sys.maxsize
# player_name = input()
#
# winner = ""
#
# while player_name != "Stop":
#     current_score = 0
#
#     for letter in player_name:
#         number = input()
#         if int(number) == ord(letter):
#             current_score += 10
#         else:
#             current_score += 2
#         if current_score >= score:
#             score = current_score
#             winner = player_name
#
#     player_name = input()
#
# print(f"The winner is {winner} with {score} points!")


player_one = input()
points_player_one = 0
points_player_two = 0
winner = ""
winner_points = 0

while player_one != "Stop":
    for letter in player_one:
        number = input()
        if ord(letter) == int(number):
            points_player_one += 10
        else:
            points_player_one += 2
    break

player_two = input()

while player_two != "Stop":
    for letter in player_two:
        number = input()
        if ord(letter) == int(number):
            points_player_two += 10
        else:
            points_player_two += 2
    break

if points_player_one > points_player_two:
    winner = player_one
    winner_points = points_player_one
elif points_player_two > points_player_one:
    winner = player_two
    winner_points = points_player_two
else:
    winner = player_two
    winner_points = points_player_two

print(f"The winner is {winner} with {winner_points} points!")

# TODO
