from math import floor

series_name = input()
num_seasons = int(input())
number_of_episodes_per_season = int(input())
length_of_episode = float(input())

ad_break_time = length_of_episode * 0.2
length_of_episode = length_of_episode + ad_break_time
added_time_special_ep = 10 * num_seasons
total_time = (length_of_episode * number_of_episodes_per_season) * num_seasons + added_time_special_ep
floor(total_time)
print(f"Total time needed to watch the {series_name} series is {int(total_time)} minutes.")
