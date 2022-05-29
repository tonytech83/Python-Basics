n = int(input())

p1_counter = 0
p2_counter = 0
p3_counter = 0
p4_counter = 0
p5_counter = 0

for num in range(n):
    current_num = int(input())

    if current_num < 200:
        p1_counter += 1
    elif current_num <= 399:
        p2_counter += 1
    elif current_num <= 599:
        p3_counter += 1
    elif current_num <= 799:
        p4_counter += 1
    else:
        p5_counter += 1

p1_percents = p1_counter / n * 100
p2_percents = p2_counter / n * 100
p3_percents = p3_counter / n * 100
p4_percents = p4_counter / n * 100
p5_percents = p5_counter / n * 100

print(f"{p1_percents:.2f}%")
print(f"{p2_percents:.2f}%")
print(f"{p3_percents:.2f}%")
print(f"{p4_percents:.2f}%")
print(f"{p5_percents:.2f}%")
