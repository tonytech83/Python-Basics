start_first = int(input())
start_second = int(input())
diff_first = int(input())
diff_second = int(input())

div_counter_first = 0
div_counter_second = 0

end_first = start_first + diff_first
end_second = start_second + diff_second

for first in range(start_first, end_first + 1):
    for second in range(start_second, end_second + 1):
        for division in range(2, first + 1):
            if first % division == 0:
                div_counter_first += 1

        for division in range(2, second + 1):
            if second % division == 0:
                div_counter_second += 1

        if div_counter_first < 2 and div_counter_second < 2:
            div_counter_first = 0
            div_counter_second = 0
            print(f'{first}{second}')

        else:
            div_counter_first = 0
            div_counter_second = 0
