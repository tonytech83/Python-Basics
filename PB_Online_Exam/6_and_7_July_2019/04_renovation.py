from math import ceil

wall_height = int(input())
wall_width = int(input())
percentage_not_painted = int(input())

total_painting = wall_height * wall_width * 4
for_painting = total_painting - ceil(total_painting * percentage_not_painted / 100)

painted = 0
console_input = ""
left_for_painting = 0

while painted <= for_painting:
    console_input = input()
    if console_input == "Tired!":
        left_for_painting = for_painting - painted
        break
    painted += int(console_input)
    left_for_painting = for_painting - painted
    if painted == left_for_painting or painted == for_painting:
        break

if console_input == "Tired!":
    print(f"{left_for_painting} quadratic m left.")
elif painted > for_painting:
    print(f"All walls are painted and you have {abs(left_for_painting)} l paint left!")
elif painted == left_for_painting or painted == for_painting:
    print(f"All walls are painted! Great job, Pesho!")
