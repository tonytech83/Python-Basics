season = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

price = 0
total = 0
sport = ''

if season == 'Winter':
    price = 9.6
    if group_type == 'mixed':
        price = 10
        sport = 'Ski'
    elif group_type == 'boys':
        sport = 'Judo'
    else:
        sport = 'Gymnastics'

elif season == 'Spring':
    price = 7.2
    if group_type == 'mixed':
        price = 9.5
        sport = 'Cycling'
    elif group_type == 'boys':
        sport = 'Tennis'
    else:
        sport = 'Athletics'

else:
    price = 15
    if group_type == 'mixed':
        price = 20
        sport = 'Swimming'
    elif group_type == 'boys':
        sport = 'Football'
    else:
        sport = 'Volleyball'

total = students_count * price * nights_count

if students_count >= 50:
    total *= 0.5
elif 20 <= students_count < 50:
    total *= 0.85
elif 10 <= students_count < 20:
    total *= 0.95

print(f'{sport} {total:.2f} lv.')
