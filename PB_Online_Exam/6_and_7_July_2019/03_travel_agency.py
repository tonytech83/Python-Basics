town = input()
package_type = input()
is_the_vip = input()
days = int(input())

price = 0
total_price = 0
valid_info = True

if package_type != "noEquipment" and package_type != "withEquipment" and package_type != "noBreakfast" and package_type != "withBreakfast":
    valid_info = False

if town == "Bansko" or town == "Borovets":
    if package_type == "withEquipment":
        price = 100
        if is_the_vip == "yes":
            price = price * 0.9
    elif package_type == "noEquipment":
        price = 80
        if is_the_vip == "yes":
            price = price * 0.95
elif town == "Varna" or town == "Burgas":
    if package_type == "withBreakfast":
        price = 130
        if is_the_vip == "yes":
            price = price * 0.88
    elif package_type == "noBreakfast":
        price = 100
        if is_the_vip == "yes":
            price = price * 0.93
else:
    valid_info = False

if days > 7:
    total_price = price * (days - 1)
else:
    total_price = price * days

if days < 1:
    print("Days must be positive number!")
else:
    if valid_info and days >= 1:
        print(f"The price is {total_price:.2f}lv! Have a nice time!")
    else:
        print(f"Invalid input!")
