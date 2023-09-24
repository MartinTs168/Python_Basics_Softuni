time_to_achieve_minutes = int(input())
time_to_achieve_seconds = int(input())
length_tunnel = float(input())
seconds_to_complete_100_meters = int(input())
time_to_achieve = time_to_achieve_seconds + time_to_achieve_minutes * 60
total_time = length_tunnel / 100 * seconds_to_complete_100_meters
removed_time = (length_tunnel / 120) * 2.5
total_time -= removed_time
if time_to_achieve >= total_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    time_needed = total_time - time_to_achieve
    print(f"No, Marin failed! He was {time_needed:.3f} second slower.")

