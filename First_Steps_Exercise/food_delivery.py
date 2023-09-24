chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15
delivery = 2.50

num_chicken_menus = int(input())
num_fish_menus = int(input())
num_vegetarian_menus = int(input())
total_price = chicken_menu_price * num_chicken_menus + \
              fish_menu_price * num_fish_menus + \
              vegetarian_menu_price * num_vegetarian_menus

total_price = total_price + (total_price * 0.20) + delivery
print(total_price)
