from math import floor

number_of_pages = int(input())
pages_read_for_1hour = int(input())
number_of_days = int(input())
hours_needed = number_of_pages/pages_read_for_1hour
hours_per_day_needed = floor(hours_needed/number_of_days)
print(hours_per_day_needed)