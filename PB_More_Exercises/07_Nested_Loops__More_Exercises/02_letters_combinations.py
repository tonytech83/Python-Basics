start = input()
end = input()
reject_letter = input()

start_to_srt = ord(start)
end_to_str = ord(end)
reject_to_str = ord(reject_letter)

counter = 0

for first in range(start_to_srt, end_to_str + 1):
    for second in range(start_to_srt, end_to_str + 1):
        for third in range(start_to_srt, end_to_str + 1):
            if first == reject_to_str or second == reject_to_str or third == reject_to_str:
                continue
            else:
                counter += 1
                print(f'{chr(first)}{chr(second)}{chr(third)}', end=' ')

print(counter)
