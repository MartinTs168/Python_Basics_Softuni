movie_name = input()
all_tickets = 0
student_ticket = 0
standard_ticket = 0
kid_ticket = 0
while not movie_name == "Finish":
    free_seats = int(input())
    tickets_sold_this_movie = 0
    for _ in range(free_seats):
        ticket_type = input()
        if ticket_type == "End":
            break
        tickets_sold_this_movie += 1
        all_tickets += 1
        if ticket_type == "student":
            student_ticket += 1
        elif ticket_type == "standard":
            standard_ticket += 1
        elif ticket_type == "kid":
            kid_ticket += 1
    left_seats = (tickets_sold_this_movie / free_seats) * 100
    print(f"{movie_name} - {left_seats:.2f}% full.")
    movie_name = input()
print(f"Total tickets: {all_tickets}")
kids_ticket_percentage = (kid_ticket / all_tickets) * 100
standard_ticket_percentage = (standard_ticket / all_tickets) * 100
student_ticket_percentage = (student_ticket / all_tickets) * 100
print(f"{student_ticket_percentage:.2f}% student tickets.")
print(f"{standard_ticket_percentage:.2f}% standard tickets.")
print(f"{kids_ticket_percentage:.2f}% kids tickets.")


