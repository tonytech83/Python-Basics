first_num = int(input())
second_num = int(input())
operator = input()

result = 0
second_num_zero = False
even_or_odd = ""

if operator == "+":
    result = first_num + second_num

elif operator == "-":
    result = first_num - second_num

elif operator == "*":
    result = first_num * second_num

elif operator == "/":
    if second_num == 0:
        second_num_zero = True
    else:
        result = first_num / second_num

elif operator == "%":
    if second_num == 0:
        second_num_zero = True
    else:
        result = first_num % second_num

if result % 2 == 0:
    even_or_odd = "even"
else:
    even_or_odd = "odd"

if operator == "+" or operator == "-" or operator == "*":
    print(f"{first_num} {operator} {second_num} = {result} - {even_or_odd}")
elif operator == "/" or operator == "%":
    if second_num_zero:
        print(f"Cannot divide {first_num} by zero")
    elif operator == "/":
        print(f"{first_num} / {second_num} = {result:.2f}")
    else:
        print(f"{first_num} % {second_num} = {result}")
