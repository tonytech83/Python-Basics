import sys

command = input()

min_number = sys.maxsize

while command != "Stop":
    command = int(command)
    if command < min_number:
        min_number = command
    command = input()

print(min_number)
