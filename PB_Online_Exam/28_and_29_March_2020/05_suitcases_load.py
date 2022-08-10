trunk_volume = float(input())

loaded_suitcases = 0
loaded_volume = 0
is_trunk_full = False

suitcase = input()

while suitcase != 'End':
    suitcase = float(suitcase)

    loaded_volume += suitcase

    if loaded_suitcases % 3 == 0:
        suitcase = suitcase * 1.1

    if loaded_volume >= trunk_volume:
        is_trunk_full = True
        break

    loaded_suitcases += 1

    suitcase = input()

if is_trunk_full:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {loaded_suitcases} suitcases loaded.")
