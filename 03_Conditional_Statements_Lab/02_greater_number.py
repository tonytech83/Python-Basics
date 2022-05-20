def greater_than(first, second):
    if first > second:
        return first
    elif second > first:
        return second
    else:
        return first


first_num = int(input())
second_number = int(input())

print(greater_than(first_num, second_number))
