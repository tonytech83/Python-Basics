n = int(input())

prev_value = int(input()) + int(input())
current_value = 0
max_diff = 0

for pair in range(n - 1):
    num_a = int(input())
    num_b = int(input())

    current_value = num_a + num_b

    if abs(prev_value - current_value) > max_diff:
        max_diff = abs(prev_value - current_value)

    prev_value = current_value

if max_diff == 0:
    print(f'Yes, value={prev_value}')
else:
    print(f'No, maxdiff={max_diff}')
