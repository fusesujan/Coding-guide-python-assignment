class Book:
    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.available = True

    def __str__(self):
        availability = "Available" if self.available else "Borrowed"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Genre: {self.genre}, Availability: {availability}"


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def get_all_books(self):
        return self.books

    def borrow_book(self, isbn):
        book = self.get_book_by_isbn(isbn)
        if book:
            if book.available:
                book.available = False
                return f"Book '{book.title}' is borrowed."
            else:
                return f"Book '{book.title}' is already borrowed."
        return "Book not found."

    def return_book(self, isbn):
        book = self.get_book_by_isbn(isbn)
        if book:
            if not book.available:
                book.available = True
                return f"Book '{book.title}' is returned successfully."
            else:
                return f"Book '{book.title}' is already available."
        return "Book not found."


class LibraryUI:
    def __init__(self):
        self.library = LibraryCatalog()

    def display_menu(self):
        print("\n1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Get Book Details")
        print("5. Display All Books")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                title = input("Enter Book Title: ")
                author = input("Enter Book Author: ")
                isbn = input("Enter ISBN: ")
                genre = input("Enter Genre: ")
                book = Book(title, author, isbn, genre)
                self.library.add_book(book)
                print(f"Book '{title}' added to the library.")

            elif choice == 2:
                isbn = input("Enter ISBN of the book to borrow: ")
                print(self.library.borrow_book(isbn))

            elif choice == 3:
                isbn = input("Enter ISBN of the book to return: ")
                print(self.library.return_book(isbn))

            elif choice == 4:
                isbn = input("Enter ISBN of the book to get details: ")
                book = self.library.get_book_by_isbn(isbn)
                if book:
                    print(book)
                else:
                    print("Book not found.")

            elif choice == 5:
                all_books = self.library.get_all_books()
                print("Here are the available books:")
                if all_books:
                    for book in all_books:
                        print(book)
                else:
                    print("No books in the library.")

            elif choice == 6:
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    ui = LibraryUI()
    ui.run()


# How it follows the single responsibility principle:



# The code you provided follows the Single Responsibility Principle (SRP) by ensuring that each class has a single responsibility and is responsible for a single actor.

# 1. **Book class:** The `Book` class is responsible for representing the attributes and behavior of a single book. Its responsibility is to hold information about a book and provide a string representation of the book when needed. It is not concerned with managing collections of books or handling user interactions.

# 2. **LibraryCatalog class:** The `LibraryCatalog` class is responsible for managing a collection of books. Its primary responsibility is to add books, retrieve book details, borrow and return books, and provide a list of all books in the library. It deals with the book collection and book availability logic. It does not handle user interface or user interactions.

# 3. **LibraryUI class:** The `LibraryUI` class is responsible for handling the user interface and user interactions. It displays a menu to the user, takes user input, and calls the appropriate methods from the `LibraryCatalog` class to perform the required operations. It does not manage the book collection or the book details directly.

# By separating the responsibilities into different classes, the code is more maintainable, modular, and easier to understand. Each class has a specific purpose and can be modified or extended independently without affecting the other classes. This adherence to SRP ensures that each class has a clear focus on its own responsibilities, making the overall code more organized and robust.