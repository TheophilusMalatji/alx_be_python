class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            return False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if book in self._books:
            print("Book already exists")
        else:
            self._books.append(book)
            print(f"Added '{book.title}' to the library.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Successfully checked out '{title}'.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book with title '{title}' not found in the library.")

    def return_book(self, title):
        # New method to find and return a book
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Successfully returned '{title}'.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book with title '{title}' not found in the library.")

    def list_available_books(self):

        available_books_found = False
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
                available_books_found = True

        if not available_books_found:
            print("No books are currently available.")


def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("\nAvailable books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    print("\nAttempting to check out '1984':")
    library.check_out_book("1984")

    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    print("\nAttempting to return '1984':")
    library.return_book("1984")

    print("\nAvailable books after returning '1984':")
    library.list_available_books()


if __name__ == "__main__":
    main()