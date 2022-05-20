def odd_or_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


number = int(input())

print(odd_or_even(number))
