class Book:
    def __init__(self, title, author):
        self._is_checked_out = False
        self.title = title
        self.author = author

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out
    

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        """Attempt to check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"'{title}' has been checked out."
                else:
                    return f"'{title}' is already checked out."
        return f"Book titled '{title}' not found."

    def return_book(self, title):
        """Return a book to the library."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return f"'{title}' has been returned."
        return f"Book titled '{title}' not found."

    def list_available_books(self):
        """List titles of books that are not checked out."""
        available = [book.title for book in self._books if book.is_available()]
        return available