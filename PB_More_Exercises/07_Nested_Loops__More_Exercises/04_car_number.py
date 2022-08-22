start = int(input())
end = int(input())

for first in range(start, end + 1):
    for second in range(start, end + 1):
        for third in range(start, end + 1):
            for fourth in range(start, end + 1):
                if first % 2 == 0 and fourth % 2 != 0 and first > fourth and (second + third) % 2 == 0:
                    print(f'{first}{second}{third}{fourth}', end=' ')
                elif first % 2 != 0 and fourth % 2 == 0 and first > fourth and (second + third) % 2 == 0:
                    print(f'{first}{second}{third}{fourth}', end=' ')
