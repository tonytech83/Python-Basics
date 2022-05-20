def check_speed(spd):
    if spd <= 10:
        return "slow"
    elif spd <= 50:
        return "average"
    elif spd <= 150:
        return "fast"
    elif spd <= 1000:
        return "ultra fast"
    else:
        return "extremely fast"


speed = float(input())

print(check_speed(speed))
