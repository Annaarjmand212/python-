running = True

while running:
    print("===== LIBRARY MANAGEMENT =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Find Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the year: "))

        new_book = Book(title, author, year)
        library.add_book(new_book)

        print("Book added successfully!")

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        book_title = input("Enter the book title: ")
        library.find_book(book_title)

    elif choice == "4":
        borrow_title = input("Enter the title: ")
        library.borrow_book(borrow_title)

    elif choice == "5":
        return_title = input("Enter the title: ")
        library.return_book(return_title)

    elif choice == "6":
        running = False
        print("Thanks for using our app!")

    else:
        print("Invalid input")