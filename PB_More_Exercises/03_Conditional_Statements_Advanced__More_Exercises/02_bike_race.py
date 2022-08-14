junior_racers = int(input())
senior_racers = int(input())
trace_type = input()

profit = 0

if trace_type == 'trail':
    profit = junior_racers * 5.5 + senior_racers * 7
elif trace_type == 'cross-country':
    if junior_racers + senior_racers >= 50:
        profit = (junior_racers * 8 + senior_racers * 9.5) * 0.75
    else:
        profit = junior_racers * 8 + senior_racers * 9.5
elif trace_type == 'downhill':
    profit = junior_racers * 12.25 + senior_racers * 13.75
else:
    profit = junior_racers * 20 + senior_racers * 21.5

profit *= 0.95

print(f'{profit:.2f}')
