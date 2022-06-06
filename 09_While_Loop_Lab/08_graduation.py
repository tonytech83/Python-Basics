student_name = input()

average_grade = 0
current_class = 1
sum_grade = 0
bad_tries = 0
is_excluded = False

while current_class <= 12:
    current_grade = float(input())

    if current_grade >= 4:
        current_class += 1
        sum_grade += current_grade
    else:
        bad_tries += 1
        if bad_tries > 1:
            is_excluded = True
            break

if is_excluded:
    print(f"{student_name} has been excluded at {current_class} grade")

else:
    average_grade = sum_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
