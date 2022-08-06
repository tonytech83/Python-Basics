visitors = int(input())

back_train = 0
chest_train = 0
legs_train = 0
abs_train = 0
protein_shake = 0
protein_bar = 0

for visitor in range(visitors):
    activity = input()
    if activity == "Back":
        back_train += 1
    elif activity == "Chest":
        chest_train += 1
    elif activity == "Legs":
        legs_train += 1
    elif activity == "Abs":
        abs_train += 1
    elif activity == "Protein shake":
        protein_shake += 1
    else:
        protein_bar += 1

print(f'{back_train} - back')
print(f'{chest_train} - chest')
print(f'{legs_train} - legs')
print(f'{abs_train} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')

percent_training = (back_train + chest_train + legs_train + abs_train) / visitors * 100
protein_buyers = (protein_shake + protein_bar) / visitors * 100

print(f"{percent_training:.2f}% - work out")
print(f'{protein_buyers:.2f}% - protein')

