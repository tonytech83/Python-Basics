groups_count = int(input())

musala = 0
monblan = 0
kalimadjaro = 0
k2 = 0
everest = 0
total_people = 0

for group in range(groups_count):
    people_in_group = int(input())
    total_people += people_in_group
    if people_in_group <= 5:
        musala += people_in_group
    elif 6 <= people_in_group <= 12:
        monblan += people_in_group
    elif 13 <= people_in_group <= 25:
        kalimadjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        k2 += people_in_group
    else:
        everest += people_in_group

percent_musala = musala / total_people * 100
percent_monblan = monblan / total_people * 100
percent_kalimadjaro = kalimadjaro / total_people * 100
percent_k2 = k2 / total_people * 100
percent_everest = everest / total_people * 100

print(f'{percent_musala:.2f}%')
print(f'{percent_monblan:.2f}%')
print(f'{percent_kalimadjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everest:.2f}%')
