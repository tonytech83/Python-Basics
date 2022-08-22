a = int(input())
b = int(input())
generated_passwords = int(input())

counter = 0
break_point = False

for first in range(35, 55):

    for second in range(64, 96):

        for third in range(1, a + 1):

            for fourth in range(1, b + 1):
                if counter >= generated_passwords:
                    break_point = True
                    break

                counter += 1

                print(f'{chr(first)}{chr(second)}{third}{fourth}{chr(second)}{chr(first)}', end='|')

                if third == a and fourth == b:
                    break_point = True
                    break

                first += 1
                if first > 55:
                    first = 35
                second += 1
                if second > 96:
                    second = 64

            if break_point:
                break

        if break_point:
            break

    if break_point:
        break
