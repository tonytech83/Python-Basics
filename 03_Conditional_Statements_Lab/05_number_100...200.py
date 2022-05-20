def check_number(num):
    if num < 100:
        return "Less than 100"
    elif 100 <= num <= 200:
        return "Between 100 and 200"
    else:
        return "Greater than 200"


number = int(input())

print(check_number(number))
