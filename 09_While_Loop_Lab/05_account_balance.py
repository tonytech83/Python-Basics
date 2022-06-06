command = input()

total = 0

while command != "NoMoreMoney":
    if float(command) < 0:
        print("Invalid operation!")
        break

    total += float(command)
    print(f"Increase: {float(command):.2f}")

    command = input()

print(f"Total: {total:.2f}")
