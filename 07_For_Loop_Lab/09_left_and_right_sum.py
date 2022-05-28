number_from_console = int(input())

left_sum = 0
right_sum = 0

for num in range(number_from_console * 2):
    current_num = int(input())
    if num < number_from_console:
        left_sum += current_num
    else:
        right_sum += current_num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
