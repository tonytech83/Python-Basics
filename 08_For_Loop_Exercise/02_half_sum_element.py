import sys

n = int(input())

max_num = -sys.maxsize
sum_of_all = 0

for num in range(n):
    current_mun = int(input())
    sum_of_all += current_mun
    if current_mun > max_num:
        max_num = current_mun

sum_of_small_muns = sum_of_all - max_num

if max_num == sum_of_small_muns:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - sum_of_small_muns)
    print("No")
    print(f"Diff = {diff}")
