from math import ceil
name_of_show = input()
episode_length = int(input())
break_length = int(input())
time_for_lunch = break_length * 1 / 8
time_for_rest = break_length * 1 / 4
time_needed = episode_length + time_for_rest + time_for_lunch
if break_length >= time_needed:
   leftover_time = break_length - time_needed

   print(f"You have enough time to watch {name_of_show} and left with {ceil(leftover_time)} minutes free time.")
else:
    extra_time = time_needed - break_length

    print(f"You don't have enough time to watch {name_of_show}, you need {ceil(extra_time)} more minutes." )
