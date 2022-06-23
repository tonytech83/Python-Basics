from math import ceil

time_for_filming = int(input())
scenes_count = int(input())
scene_time = int(input())

time_after_preparation = time_for_filming * 0.85

diff = abs(time_after_preparation - scenes_count * scene_time)

if time_after_preparation > scenes_count * scene_time:

    print(f"You managed to finish the movie on time! You have {ceil(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {ceil(diff)} minutes.")
