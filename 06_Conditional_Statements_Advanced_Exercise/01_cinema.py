ticket_type = input()
rows = int(input())
cols = int(input())

movie_theater = rows * cols
ticket_price = 0

if ticket_type == "Premiere":
    ticket_price = 12
elif ticket_type == "Normal":
    ticket_price = 7.5
else:
    ticket_price = 5

print(f"{(movie_theater * ticket_price):.2f} leva")
