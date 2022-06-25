needed_processors = int(input())
employees = int(input())
working_days = int(input())

total_working_hours = working_days * employees * 8
manufactured_processors = int(total_working_hours / 3)

diff = abs(needed_processors - manufactured_processors) * 110.10

if manufactured_processors >= needed_processors:
    print(f"Profit: -> {diff:.2f} BGN")
else:
    print(f"Losses: -> {diff:.2f} BGN")
