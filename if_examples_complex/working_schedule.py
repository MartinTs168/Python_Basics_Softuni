hour = int(input())
day = input()
if day == "Sunday":
    print("closed")
elif 10<= hour <= 18:
    print("open")
else:
    print("closed")

# this solution of the task is incorrect but it works. it is Incorrect because it will still work if you enter random string as day

hour = int(input())
day = input()
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
    if 10<= hour <= 18:
        print("open")
    else:
        print("closed")
elif day == "Sunday":
    print("closed")

# this is a more correct way to solve the task.