from math import ceil

tv_serial_name = input()
tv_duration = int(input())
lunch_time = int(input())

lunch_duration = lunch_time / 8
break_duration = lunch_time / 4

time_for_watching = lunch_time - lunch_duration - break_duration
diff_1 = ceil(tv_duration - time_for_watching)
diff_2 = ceil(time_for_watching - tv_duration)


if time_for_watching >= tv_duration:
    print(f"You have enough time to watch {tv_serial_name} and left with {diff_2} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_serial_name}, you need {diff_1} more minutes.")

