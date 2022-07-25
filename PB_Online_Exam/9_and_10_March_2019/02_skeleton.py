quota_time_minutes = int(input())
quota_time_seconds = int(input())
track_in_meters = float(input())
seconds_per_100 = int(input())

converted_time_sec = quota_time_minutes * 60 + quota_time_seconds
time_reduction = track_in_meters / 120 * 2.5

total_time = track_in_meters / 100 * seconds_per_100 - time_reduction

if total_time <= converted_time_sec:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    needed_time = abs(converted_time_sec - total_time)
    print(f"No, Marin failed! He was {needed_time:.3f} second slower.")
