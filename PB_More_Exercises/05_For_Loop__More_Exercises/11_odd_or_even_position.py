import sys

n = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for number in range(1, n + 1):

    num = float(input())

    if number % 2 != 0:
        odd_sum += num
        if num < odd_min:
            odd_min = num
        if num > odd_max:
            odd_max = num

    else:
        even_sum += num
        if num < even_min:
            even_min = num
        if num > even_max:
            even_max = num

print(f'OddSum={odd_sum:.2f},')
if odd_sum == 0:
    print('OddMin=No,')
    print('OddMax=No,')
else:
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
print(f'EvenSum={even_sum:.2f},')
if even_sum == 0:
    print('EvenMin=No,')
    print('EvenMax=No')
else:
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')
