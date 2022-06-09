bad_grades = int(input())
exam_name = input()

bad_grades_count = 0
grades_sum = 0
grades_count = 0
last_exam = ""

while exam_name != "Enough":

    current_grade = int(input())
    grades_sum += current_grade
    grades_count += 1
    if current_grade <= 4:
        bad_grades_count += 1
        if bad_grades_count == bad_grades:
            break
    last_exam = exam_name
    exam_name = input()

average_grade = grades_sum / grades_count

if exam_name == "Enough":
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {grades_count}")
    print(f"Last problem: {last_exam}")
else:
    print(f"You need a break, {bad_grades_count} poor grades.")
