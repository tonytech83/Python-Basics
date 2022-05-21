day_of_week = input()

price = 0

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Friday":
    price = 12
elif day_of_week == "Wednesday" or day_of_week == "Thursday":
    price = 14
else:
    price = 16

print(price)
