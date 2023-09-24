book_to_search = input()
books = input()
not_found = False
book_counter = 0
while books != book_to_search:
    if books == "No More Books":
        not_found = True
        break
    book_counter += 1
    books = input()

if not_found:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")
else:
    print(f"You checked {book_counter} books and found it.")