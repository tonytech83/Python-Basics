n = int(input())

sum = 0

for _ in range(n):
    num = int(input())
    sum += num

average = sum / n

print(f'{average:.2f}')
