import sys

films_count = int(input())

high_rating = 0
low_rating = sys.maxsize

sum_ratings = 0

high_rating_film = ""
low_rating_film = ""

for film in range(films_count):
    current_film_name = input()
    current_film_rating = float(input())
    if current_film_rating < low_rating:
        low_rating_film = current_film_name
        low_rating = current_film_rating

    sum_ratings += current_film_rating

    if current_film_rating > high_rating:
        high_rating_film = current_film_name
        high_rating = current_film_rating


average_rating = sum_ratings / films_count

print(f"{high_rating_film} is with highest rating: {high_rating:.1f}")
print(f"{low_rating_film} is with lowest rating: {low_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
