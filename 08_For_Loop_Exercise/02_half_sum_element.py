n = int(input())

max_num = 0
sum_of_small_nums = 0

for num in range(n):
    current_mun = int(input())
    sum_of_small_nums += current_mun
    if current_mun > max_num:
        max_num = current_mun

sum_of_small_nums -= max_num

if max_num == sum_of_small_nums:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - sum_of_small_nums)
    print("No")
    print(f"Diff = {diff}")
