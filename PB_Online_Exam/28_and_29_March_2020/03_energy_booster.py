fruit = input()
package_size = input()
package_count = int(input())

total = 0

if package_size == "small":
    if fruit == "Watermelon":
        total = package_count * 56 * 2
    elif fruit == "Mango":
        total = package_count * 36.66 * 2
    elif fruit == "Pineapple":
        total = package_count * 42.10 * 2
    else:
        total = package_count * 20 * 2
else:
    if fruit == "Watermelon":
        total = package_count * 28.7 * 5
    elif fruit == "Mango":
        total = package_count * 19.6 * 5
    elif fruit == "Pineapple":
        total = package_count * 24.8 * 5
    else:
        total = package_count * 15.2 * 5

if 400 <= total <= 1000:
    total *= 0.85
elif total > 1000:
    total *= 0.5

print(f'{total:.2f} lv.')
