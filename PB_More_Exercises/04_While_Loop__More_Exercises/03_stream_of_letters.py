from collections import deque

secret = []

letter = input()

command = ['c', 'o', 'n']

test = ord(letter)

while letter != "End":

    if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
        if letter not in command:
            secret.append(letter)
        else:
            command.remove(letter)

    if command == []:
        command = ['c', 'o', 'n']
        print(*secret, sep='', end='')
        print(' ', end='')
        secret.clear()

    letter = input()
