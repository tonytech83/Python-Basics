locations_count = int(input())

for location in range(locations_count):
    expected_average_yield = float(input())  # per day
    working_days = int(input())

    location_yield = 0

    for day in range(working_days):
        yield_per_day = float(input())
        location_yield += yield_per_day

    location_average_yield = location_yield / working_days

    if location_average_yield >= expected_average_yield:
        print(f"Good job! Average gold per day: {location_average_yield:.2f}.")
    else:
        diff = expected_average_yield - location_average_yield
        print(f"You need {diff:.2f} gold.")
