

record = float(input())
distance = float(input())
seconds_per_meter = float(input())
WATER_RESISTANCE_TIME_LOST = 12.5

extra_time = (distance // 15) * WATER_RESISTANCE_TIME_LOST
time_attempt = distance * seconds_per_meter + extra_time
if record > time_attempt:
    print(f"Yes, he succeeded! The new world record is {time_attempt:.2f} seconds.")
elif record <= time_attempt:
    seconds_behind_record = time_attempt - record
    print(f"No, he failed! He was {seconds_behind_record:.2f} seconds slower.")
