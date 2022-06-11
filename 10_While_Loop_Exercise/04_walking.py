command = input()

steps = 0
goal_reached = False

while command != "Going home":
    steps += int(command)
    if steps >= 10000:
        goal_reached = True
        break
    else:
        command = input()

if goal_reached:
    diff = abs(10000 - steps)
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    command = int(input())
    steps += command
    if steps > 10000:
        diff = abs(10000 - steps)
        print(f"Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
    else:
        diff = 10000 - steps
        print(f"{diff} more steps to reach goal.")

