wanted_book = input()
next_book = input()

find_book = True
checked_books = 0

while next_book != wanted_book:
    next_book = input()
    checked_books += 1
    if next_book == "No More Books":
        find_book = False
        break

if find_book:
    print(f"You checked {checked_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {checked_books} books.")
