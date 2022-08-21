n = int(input())

print('*' * n * 2 + ' ' * n + '*' * n * 2)

for row in range(n - 2):
    if row == (n - 1) // 2 - 1:
        print('*' + "/" * (n * 2 - 2) + '*' + '|' * n + '*' + '/' * (n * 2 - 2) + '*')
    else:
        print('*' + "/" * (n * 2 - 2) + '*' + ' ' * n + '*' + '/' * (n * 2 - 2) + '*')

print('*' * n * 2 + ' ' * n + '*' * n * 2)
