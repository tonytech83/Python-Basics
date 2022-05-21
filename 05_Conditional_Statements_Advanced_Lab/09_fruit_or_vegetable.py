item = input()

fruit = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetable = ["tomato", "cucumber", "pepper", "carrot"]

if item in fruit:
    print("fruit")
elif item in vegetable:
    print("vegetable")
else:
    print("unknown")
