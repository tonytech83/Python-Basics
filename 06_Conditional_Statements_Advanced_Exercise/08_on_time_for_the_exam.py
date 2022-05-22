exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

# convert hours in minutes and calculate time
exam_time_to_minutes = exam_hours * 60 + exam_minutes
arrival_time_to_minutes = arrival_hours * 60 + arrival_minutes
minutes_diff = abs(exam_time_to_minutes - arrival_time_to_minutes)

hours = minutes_diff // 60
minutes = minutes_diff % 60

# check the status of arrival
if 0 <= (exam_time_to_minutes - arrival_time_to_minutes) <= 30:
    print("On time")
    if minutes_diff != 0:
        print(f"{minutes_diff} minutes before the start")

elif arrival_time_to_minutes < exam_time_to_minutes:
    print("Early")
    if minutes_diff < 60:
        print(f"{minutes_diff} minutes before the start")
    else:
        if minutes < 10:
            print(f"{hours}:0{minutes} hours before the start")
        else:
            print(f"{hours}:{minutes} hours before the start")

elif arrival_time_to_minutes > exam_time_to_minutes:
    print("Late")
    if minutes_diff < 60:
        print(f"{minutes_diff} minutes after the start")
    else:
        if minutes < 10:
            print(f"{hours}:0{minutes} hours after the start")
        else:
            print(f"{hours}:{minutes} hours after the start")
