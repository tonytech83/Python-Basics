import math

current_word = input()

current_word_power = 0
the_power_word = ""
the_power_word_points = 0

vowel_list = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']

while current_word != "End of words":
    current_word_power = 0
    for letter in current_word:
        current_word_power += ord(letter)

    first_char = current_word[0]
    if first_char in vowel_list:
        current_word_power = current_word_power * len(current_word)
    else:
        current_word_power = math.floor(current_word_power / 3)

    if current_word_power > the_power_word_points:
        the_power_word = current_word
        the_power_word_points = current_word_power

    current_word = input()

print(f"The most powerful word is {the_power_word} - {the_power_word_points}")
