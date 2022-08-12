from math import floor

w = float(input()) * 100
h = float(input()) * 100

rows = floor((h - 100) / 70)
cols = floor(w / 120)

usable_space = rows * cols - 3

print(usable_space)
