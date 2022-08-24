n = int(input())
l = int(input())

for one in range(1, n + 1):
    for two in range(1, n + 1):
        for three in range(97, (97 + l)):
            for fourth in range(97, (97 + l)):
                for five in range(1, n + 1):
                    if five > one and five > two:
                        print(f'{one}{two}{chr(three)}{chr(fourth)}{five}', end=' ')
