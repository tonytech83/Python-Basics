weekend_days = int(input())
normal_playing_time = 30000

working_days = 365 - weekend_days

playing_time = weekend_days * 127 + working_days * 63

diff = abs(normal_playing_time - playing_time)
hours = diff // 60
minutes = diff % 60

if playing_time <= normal_playing_time:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
