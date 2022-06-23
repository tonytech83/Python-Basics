film_name = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
cinema_percent = int(input())

tickets_price_per_day = tickets * ticket_price
tickets_for_period = days * tickets_price_per_day

income = tickets_for_period - tickets_for_period * cinema_percent / 100

print(f"The profit from the movie {film_name} is {income:.2f} lv.")
