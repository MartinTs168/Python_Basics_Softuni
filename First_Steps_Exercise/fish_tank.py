length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent_taken_space = float(input()) / 100
aquarium_volume = (length_cm * width_cm * height_cm) / 1000
needed_liters = aquarium_volume * (1 - percent_taken_space)
print(needed_liters)
