one_amount = int(input())
two_amount = int(input())
five_amount = int(input())
amount = int(input())

for one in range(0, one_amount + 1):
    for two in range(0, two_amount + 1):
        for five in range(0, five_amount + 1):
            if (one * 1 + two * 2 + five * 5) == amount:
                print(f'{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {amount} lv.')
