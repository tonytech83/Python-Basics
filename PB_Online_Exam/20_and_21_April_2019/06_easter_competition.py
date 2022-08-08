bake_count = int(input())

best_baker = None
best_points = 0

for bake in range(bake_count):
    baker_name = input()
    points = 0
    current_points = input()
    while current_points != 'Stop':
        points += int(current_points)

        current_points = input()

    print(f'{baker_name} has {points} points.')

    if points > best_points:
        best_points = points
        best_baker = baker_name
        print(f'{best_baker} is the new number 1!')

print(f'{best_baker} won competition with {best_points} points!')
