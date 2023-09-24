from math import pi

type_of_figure = input()
area = 0
if type_of_figure == "square":
    side = float(input())
    area = side * side
elif type_of_figure == "rectangle":
    side = float(input())
    side_2 = float(input())
    area = side * side_2
elif type_of_figure == "circle":
    radius = float(input())
    area = radius ** 2 * pi

elif type_of_figure == "triangle":
    side = float(input())
    height = float(input())
    area = (side * height) / 2
print(f"{area:.3f}")
