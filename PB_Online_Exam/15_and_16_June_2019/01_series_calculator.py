series_name = input()
series_seasons = int(input())
series_episodes = int(input())
episode_time = float(input())

normal_episode_time = episode_time * 1.2
special_episode_time = series_seasons * 10

total_time = normal_episode_time * series_episodes * series_seasons + special_episode_time

print(f"Total time needed to watch the {series_name} series is {int(total_time)} minutes.")
