from math import floor

record_time = float(input())
track = float(input())
time_per_meter = float(input())

slowdown = floor(track // 50) * 30

total_time = track * time_per_meter + slowdown

if total_time < record_time:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    diff = abs(record_time - total_time)
    print(f'No! He was {diff:.2f} seconds slower.')
