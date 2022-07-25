nation = input()
gymnastic_item = input()
team_points = 0

if nation == "Bulgaria":
    if gymnastic_item == "ribbon":
        team_points = 9.6 + 9.4
    elif gymnastic_item == "hoop":
        team_points = 9.55 + 9.75
    else:
        team_points = 9.5 + 9.4
elif nation == "Russia":
    if gymnastic_item == "ribbon":
        team_points = 9.1 + 9.4
    elif gymnastic_item == "hoop":
        team_points = 9.3 + 9.8
    else:
        team_points = 9.6 + 9
else:
    if gymnastic_item == "ribbon":
        team_points = 9.2 + 9.5
    elif gymnastic_item == "hoop":
        team_points = 9.45 + 9.35
    else:
        team_points = 9.7 + 9.15

percent_to_max = 100 - (team_points / 20 * 100)

print(f"The team of {nation} get {team_points:.3f} on {gymnastic_item}.")
print(f"{percent_to_max:.2f}%")
