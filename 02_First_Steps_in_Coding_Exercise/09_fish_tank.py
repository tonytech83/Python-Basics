length = int(input())
width = int(input())
height = int(input())
percent_acc = float(input())

volume = length * width * height
volume_in_letters = volume / 1000
volume_acc = volume_in_letters * percent_acc / 100

result = volume_in_letters - volume_acc

print(result)

