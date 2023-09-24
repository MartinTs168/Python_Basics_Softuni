width_of_free_space = int(input())
length_of_free_space = int(input())
height_of_free_space = int(input())
box_area = 1
free_space_area = width_of_free_space * length_of_free_space * height_of_free_space
free_space_available = free_space_area // box_area
command = input()
while not command == "Done":
    boxes_moved = int(command)
    free_space_available -= boxes_moved
    if free_space_available <= 0:
        print(f"No more free space! You need {-free_space_available} Cubic meters more.")
        break
    command = input()
else:
    print(f"{free_space_available} Cubic meters left.")

