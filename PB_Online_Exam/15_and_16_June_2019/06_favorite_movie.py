best_movie_points = 0
best_movie = None

is_hit_limit = False

for movie in range(7):
    movie_name = input()

    if movie_name == "STOP":
        break

    current_movie_points = 0

    for letter in movie_name:

        if 65 <= ord(letter) <= 90:
            current_movie_points += ord(letter) - len(movie_name)
        elif 97 <= ord(letter) <= 122:
            current_movie_points += ord(letter) - len(movie_name) * 2
        else:
            current_movie_points += ord(letter)

    if current_movie_points > best_movie_points:
        best_movie_points = current_movie_points
        best_movie = movie_name

    if movie == 6:
        is_hit_limit = True

if is_hit_limit:
    print("The limit is reached.")

print(f'The best movie for you is {best_movie} with {best_movie_points} ASCII sum.')
