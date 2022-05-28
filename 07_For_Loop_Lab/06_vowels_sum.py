text_from_console = input()

sum_of_vowels = 0

for letter in text_from_console:
    if letter == "a":
        sum_of_vowels += 1
    elif letter == "e":
        sum_of_vowels += 2
    elif letter == "i":
        sum_of_vowels += 3
    elif letter == "o":
        sum_of_vowels += 4
    elif letter == "u":
        sum_of_vowels += 5

print(sum_of_vowels)
