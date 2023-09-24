cake_width = int(input())
cake_length = int(input())
piece_size = 1
cake_size = cake_length * cake_width
pieces_available = cake_size // piece_size
command = input()
while not command == "STOP":
    pieces_taken = int(command)
    pieces_available -= pieces_taken
    if pieces_available <= 0:
        print(f"No more cake left! You need {-pieces_available} pieces more.")
        break
    command = input()
else:
    print(f"{pieces_available} pieces are left.")
