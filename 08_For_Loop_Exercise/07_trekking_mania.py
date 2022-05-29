count_of_groups = int(input())

goto_musala = 0
goto_monblan = 0
goto_kilimandjaro = 0
goto_k2 = 0
goto_everest = 0
total_people = 0

for group in range(count_of_groups):
    number_of_people = int(input())
    total_people += number_of_people

    if number_of_people <= 5:
        goto_musala += number_of_people
    elif number_of_people <= 12:
        goto_monblan += number_of_people
    elif number_of_people <= 25:
        goto_kilimandjaro += number_of_people
    elif number_of_people <= 40:
        goto_k2 += number_of_people
    else:
        goto_everest += number_of_people

print(f"{(goto_musala / total_people * 100):.2f}%")
print(f"{(goto_monblan / total_people * 100):.2f}%")
print(f"{(goto_kilimandjaro / total_people * 100):.2f}%")
print(f"{(goto_k2 / total_people * 100):.2f}%")
print(f"{(goto_everest / total_people * 100):.2f}%")
