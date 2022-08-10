joinery_count = int(input())
joinery_type = input()
delivery = input()

is_invalid_order = False

if joinery_count < 10:
    is_invalid_order = True

if joinery_type == '90X130':

    price = 110

    if 30 < joinery_count <= 60:
        price *= 0.95
    elif joinery_count > 60:
        price *= 0.92

elif joinery_type == '100X150':

    price = 140

    if 40 < joinery_count <= 80:
        price *= 0.94
    elif joinery_count > 80:
        price *= 0.9

elif joinery_type == '130X180':

    price = 190

    if 20 < joinery_count <= 50:
        price *= 0.93
    elif joinery_count > 50:
        price *= 0.88

else:

    price = 250

    if 25 < joinery_count <= 50:
        price *= 0.91
    elif joinery_count > 50:
        price *= 0.86

total_price = joinery_count * price

if delivery == 'With delivery':
    total_price += 60

if joinery_count > 99:
    total_price *= 0.96

if is_invalid_order:
    print("Invalid order")
else:
    print(f'{total_price:.2f} BGN')
