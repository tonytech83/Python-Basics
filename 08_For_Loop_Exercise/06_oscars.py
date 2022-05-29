actor_name = input()
points_from_academy = float(input())
num_of_evaluators = int(input())

# points_from_academy = 0

for actor in range(num_of_evaluators):
    evaluator_name = input()
    evaluator_points = float(input())
    points_from_academy += (len(evaluator_name) * evaluator_points / 2)
    if points_from_academy >= 1250.5:
        break

if points_from_academy >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points_from_academy:.1f}!")
else:
    necessary_points = 1250.5 - points_from_academy
    print(f"Sorry, {actor_name} you need {necessary_points:.1f} more!")
