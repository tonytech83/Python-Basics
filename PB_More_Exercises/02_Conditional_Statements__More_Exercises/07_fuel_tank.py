fuel_type = input().lower()
fuel_in_tank = float(input())

fuel_types = ['diesel', 'gasoline', 'gas']

if fuel_type in fuel_types:
    if fuel_in_tank >= 25:
        print(f'You have enough {fuel_type}.')
    else:
        print(f'Fill your tank with {fuel_type}!')
else:
    print('Invalid fuel!')
