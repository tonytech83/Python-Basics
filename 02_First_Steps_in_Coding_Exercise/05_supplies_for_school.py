pen_packages = int(input())
markers_packages = int(input())
cleaning_fluid = int(input())
percent_discount = int(input())

price_of_pens = pen_packages * 5.80
price_of_markers = markers_packages * 7.20
price_of_fluid = cleaning_fluid * 1.20

total_without_discount = price_of_pens + price_of_markers + price_of_fluid
total_with_discount = total_without_discount - (total_without_discount * percent_discount / 100)

print(f"{total_with_discount:.2f}")
