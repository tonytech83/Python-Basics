free_width = int(input())
free_length = int(input())
free_height = int(input())

free_area = free_width * free_length * free_height

boxes = int(input())
is_enough_free_space = True

while boxes != "Done":
    free_area -= int(boxes)
    if free_area < 0:
        is_enough_free_space = False
        break
    boxes = input()

if is_enough_free_space:
    print(f"{free_area} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_area)} Cubic meters more.")