destination = input()
money_needed = float(input())
saved_today = float(input())
saved_total = saved_today
while True:
    while money_needed > saved_total:
        saved_today = float(input())
        saved_total += saved_today
    print(f"Going to {destination}!")
    saved_total = 0
    destination = input()
    if destination == "End":
        break
    money_needed = float(input())

