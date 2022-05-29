n = int(input())

counter_p1 = 0
counter_p2 = 0
counter_p3 = 0
counter_p4 = 0
counter_p5 = 0

for num in range(n):
    current_num = int(input())

    if current_num < 200:
        counter_p1 += 1
    elif current_num <= 399:
        counter_p2 += 1
    elif current_num <= 599:
        counter_p3 += 1
    elif current_num <= 799:
        counter_p4 += 1
    else:
        counter_p5 += 1

p1_percents = counter_p1 / n * 100
p2_percents = counter_p2 / n * 100
p3_percents = counter_p3 / n * 100
p4_percents = counter_p4 / n * 100
p5_percents = counter_p5 / n * 100

print(f"{p1_percents:.2f}%")
print(f"{p2_percents:.2f}%")
print(f"{p3_percents:.2f}%")
print(f"{p4_percents:.2f}%")
print(f"{p5_percents:.2f}%")
