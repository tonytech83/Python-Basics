import sys

score = -sys.maxsize
player_name = input()

winner = ""

while player_name != "Stop":
    current_score = 0

    for letter in player_name:
        number = input()
        if int(number) == ord(letter):
            current_score += 10
        else:
            current_score += 2
        if current_score >= score:
            score = current_score
            winner = player_name

    player_name = input()

print(f"The winner is {winner} with {score} points!")
