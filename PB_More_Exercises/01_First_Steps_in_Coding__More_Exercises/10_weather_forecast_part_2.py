degrees = float(input())

if 5 <= degrees <= 11.9:
    print('Cold')
elif 12 <= degrees <= 14.9:
    print('Cool')
elif 15 <= degrees <= 20:
    print('Mild')
elif 20.1 <= degrees <= 25.9:
    print('Warm')
elif 26 <= degrees <= 35:
    print('Hot')
else:
    print('unknown')
