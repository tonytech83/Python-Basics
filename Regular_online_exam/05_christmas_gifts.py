command = input()

kids = 0
adults = 0

toys_price = 0
pullover_price = 0

while command != "Christmas":
    age = int(command)
    if age <= 16:
        kids += 1
        toys_price += 5
    else:
        adults += 1
        pullover_price += 15

    command = input()

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {toys_price}")
print(f"Money for sweaters: {pullover_price}")
