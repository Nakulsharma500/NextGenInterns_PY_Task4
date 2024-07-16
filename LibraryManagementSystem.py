class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Initially all books are available

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Book added successfully: {new_book}")

    def display_available_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books in the library:")
            for book in self.books:
                if book.available:
                    print(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print(f"Book '{book.title}' borrowed successfully.")
                else:
                    print(f"Sorry, '{book.title}' is currently not available.")
                return
        print("Book with ISBN not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    print(f"Book '{book.title}' returned successfully.")
                else:
                    print(f"Book '{book.title}' is already available in the library.")
                return
        print("Book with ISBN not found.")

def main():
    library = Library()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add a Book")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Display Available Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter title of the book: ")
            author = input("Enter author of the book: ")
            isbn = input("Enter ISBN of the book: ")
            library.add_book(title, author, isbn)
        elif choice == '2':
            isbn = input("Enter ISBN of the book you want to borrow: ")
            library.borrow_book(isbn)
        elif choice == '3':
            isbn = input("Enter ISBN of the book you want to return: ")
            library.return_book(isbn)
        elif choice == '4':
            library.display_available_books()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
