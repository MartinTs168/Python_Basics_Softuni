price_for_packet_of_pens = 5.80
price_for_packet_of_markers = 7.20
price_for_cleaning_spray_per_liter = 1.20
packets_of_pens = int(input())
packets_of_markers = int(input())
liters_of_cleaning_spray = int(input())
discount = int(input())/100
price_of_pens = price_for_packet_of_pens * packets_of_pens
price_of_markers = price_for_packet_of_markers * packets_of_markers
price_of_cleaning_spray = price_for_cleaning_spray_per_liter * liters_of_cleaning_spray
full_price = price_of_pens + price_of_markers + price_of_cleaning_spray - (
    (price_of_pens + price_of_markers + price_of_cleaning_spray) * discount)
print(full_price)
