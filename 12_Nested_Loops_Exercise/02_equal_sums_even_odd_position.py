number_1 = int(input())
number_2 = int(input())

for num in range(number_1, number_2 + 1):
    num_to_str = str(num)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(num_to_str):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum:
        print(num, end=" ")
