numbers = int(input())

p1 = 0
p2 = 0
p3 = 0

for number in range(numbers):
    current_number = int(input())
    if current_number % 2 == 0:
        p1 += 1
    if current_number % 3 == 0:
        p2 += 1
    if current_number % 4 == 0:
        p3 += 1

p1_percent = p1 / numbers * 100
p2_percent = p2 / numbers * 100
p3_percent = p3 / numbers * 100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
