hour = int(input())
day_of_week = input()

if day_of_week == "Sunday":
    print("closed")
else:
    if 10 <= hour <= 18:
        print("open")
    else:
        print("closed")
