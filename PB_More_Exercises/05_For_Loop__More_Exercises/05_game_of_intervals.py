game_turns = int(input())

result = 0
interval_1 = 0
interval_2 = 0
interval_3 = 0
interval_4 = 0
interval_5 = 0
interval_6 = 0

for turn in range(game_turns):
    current_turn = int(input())
    if 0 <= current_turn < 10:
        result += current_turn * 0.2
        interval_1 += 1
    elif 10 <= current_turn < 20:
        result += current_turn * 0.3
        interval_2 += 1
    elif 20 <= current_turn < 30:
        result += current_turn * 0.4
        interval_3 += 1
    elif 30 <= current_turn < 40:
        result += 50
        interval_4 += 1
    elif 40 <= current_turn <= 50:
        result += 100
        interval_5 += 1
    else:
        result /= 2
        interval_6 += 1

percent_interval_1 = interval_1 / game_turns * 100
percent_interval_2 = interval_2 / game_turns * 100
percent_interval_3 = interval_3 / game_turns * 100
percent_interval_4 = interval_4 / game_turns * 100
percent_interval_5 = interval_5 / game_turns * 100
percent_interval_6 = interval_6 / game_turns * 100

print(f'{result:.2f}')
print(f'From 0 to 9: {percent_interval_1:.2f}%')
print(f'From 10 to 19: {percent_interval_2:.2f}%')
print(f'From 20 to 29: {percent_interval_3:.2f}%')
print(f'From 30 to 39: {percent_interval_4:.2f}%')
print(f'From 40 to 50: {percent_interval_5:.2f}%')
print(f'Invalid numbers: {percent_interval_6:.2f}%')
