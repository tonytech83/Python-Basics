students_count = int(input())

fail = 0
top = 0
between_1 = 0  # Between 3.00 and 3.99
between_2 = 0  # Between 4.00 and 4.99
total = 0

for student in range(students_count):
    grade = float(input())

    total += grade

    if 2 <= grade <= 2.99:
        fail += 1
    elif 3 <= grade <= 3.99:
        between_1 += 1
    elif 4 <= grade <= 4.99:
        between_2 += 1
    elif grade >= 5:
        top += 1

average = total / students_count

print(f'Top students: {(top / students_count * 100):.2f}%')
print(f'Between 4.00 and 4.99: {(between_2 / students_count * 100):.2f}%')
print(f'Between 3.00 and 3.99: {(between_1 / students_count * 100):.2f}%')
print(f'Fail: {(fail / students_count * 100):.2f}%')
print(f'Average: {average:.2f}')
