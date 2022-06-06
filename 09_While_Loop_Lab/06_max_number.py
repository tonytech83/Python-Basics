import sys

command = input()

max_number = -sys.maxsize

while command != "Stop":
    command = int(command)
    if command > max_number:
        max_number = command
    command = input()

print(max_number)
