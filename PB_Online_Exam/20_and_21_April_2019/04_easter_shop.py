available_eggs = int(input())
sold_eggs = 0

no_more_eggs = False

command = input()

while command != "Close":
    eggs = int(input())

    if command == "Buy":
        available_eggs -= eggs
        sold_eggs += eggs
    else:
        available_eggs += eggs

    if available_eggs < 0:
        available_eggs += eggs
        no_more_eggs = True
        break

    command = input()

if no_more_eggs:
    print('Not enough eggs in store!')
    print(f'You can buy only {available_eggs}.')
else:
    print('Store is closed!')
    print(f'{sold_eggs} eggs sold.')
