hour_of_test = int(input())
minute_of_test = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())
on_time = True
test_begins = hour_of_test * 60 + minute_of_test
arrival = hour_of_arrival * 60 + minute_of_arrival
difference_in_time = test_begins - arrival
if 0 <= difference_in_time <= 30:
    print("On time")
    # print(f"{abs(difference_in_time)} minutes before the start")
elif test_begins > arrival and difference_in_time > 30:
    print("Early")
   # print(f"{difference_in_time // 60}:{difference_in_time % 60} hours before the start")
else:
    print("Late")
    on_time = False
    # print(f"{abs(difference_in_time)} hours after the start")
difference_in_time = abs(difference_in_time)
if difference_in_time == 0:
    pass
elif difference_in_time < 60:
    if on_time:
        print(f"{difference_in_time} minutes before the start")
    elif not on_time:
        print(f"{difference_in_time} minutes after the start")
else:
    if on_time:
        print(f"{difference_in_time // 60}:{difference_in_time % 60:02d} hours before the start")
    elif not on_time:
        print(f"{difference_in_time // 60}:{difference_in_time % 60:02d} hours after the start")
