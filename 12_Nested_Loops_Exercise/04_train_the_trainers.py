jury_count = int(input())

average_for_presentation = 0
average_for_all = 0
total_score_of_average = 0
score_per_presentation = 0
presentation_count = 0

presentation_name = input()

while presentation_name != "Finish":
    presentation_count += 1
    score_per_presentation = 0
    average_for_presentation = 0
    for presentation in range(1, jury_count + 1):
        current_jury_score = float(input())
        score_per_presentation += current_jury_score

    average_for_presentation = score_per_presentation / jury_count
    print(f"{presentation_name} - {average_for_presentation:.2f}.")
    total_score_of_average += average_for_presentation

    presentation_name = input()

final_assessment = total_score_of_average / presentation_count
print(f"Student's final assessment is {final_assessment:.2f}.")
