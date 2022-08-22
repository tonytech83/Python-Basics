males = int(input())
women = int(input())
table_count = int(input())

counter = 0

for male in range(1, males + 1):
    for woman in range(1, women + 1):
        counter += 1
        if counter > table_count:
            break
        print(f'({male} <-> {woman})', end=' ')

