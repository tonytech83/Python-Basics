start = input()
end = input()

for first_pair in range(int(start[0]), int(end[0]) + 1):
    for second_pair in range(int(start[1]), int(end[1]) + 1):
        for third_pair in range(int(start[2]), int(end[2]) + 1):
            for fourth_pair in range(int(start[3]), int(end[3]) + 1):
                if first_pair % 2 != 0 and second_pair % 2 != 0 and third_pair % 2 != 0 and fourth_pair % 2 != 0:
                    print(f'{first_pair}{second_pair}{third_pair}{fourth_pair}', end=' ')
