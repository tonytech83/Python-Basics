target_high = int(input())
is_success = False
tries = 0
workout_jump = target_high - 30
failed_jumps = 0

while True:
    jump = int(input())
    tries += 1

    if jump > workout_jump:
        workout_jump += 5
        failed_jumps = 0
    else:
        failed_jumps += 1
        if failed_jumps == 3:
            break

    if workout_jump > target_high:
        is_success = True
        break

if is_success:
    print(f'Tihomir succeeded, he jumped over {target_high}cm after {tries} jumps.')
else:
    print(f'Tihomir failed at {workout_jump}cm after {tries} jumps.')
