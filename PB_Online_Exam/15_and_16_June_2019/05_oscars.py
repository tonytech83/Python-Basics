actor_name = input()
academy_points = float(input())
evaluators = int(input())

total_points = academy_points
is_nominated = False

for evaluator in range(evaluators):
    evaluator_name = input()
    evaluator_points = float(input())
    total_points += len(evaluator_name) * evaluator_points / 2
    if total_points > 1250.5:
        is_nominated = True
        break

if is_nominated:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - total_points):.1f} more!")
