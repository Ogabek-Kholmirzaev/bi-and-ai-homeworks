class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {'Borrowed' if self.is_borrowed else 'Available'})"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("A member can borrow a maximum of 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

    def __repr__(self):
        return f"Member({self.name}, Borrowed Books: {len(self.borrowed_books)})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"The book '{title}' was not found in the library.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")
        book = self.find_book(book_title)
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")
        book = self.find_book(book_title)
        member.return_book(book)

    def __repr__(self):
        return f"Library(Books: {len(self.books)}, Members: {len(self.members)})"

library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.add_member(Member("Alice"))

try:
    library.borrow_book("Alice", "1984")
    print("Alice borrowed '1984'.")
    library.borrow_book("Alice", "1984")
except Exception as e:
    print(f"Error: {e}")

try:
    library.borrow_book("Alice", "Nonexistent Book")
except Exception as e:
    print(f"Error: {e}")

try:
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "Another Book")
except Exception as e:
    print(f"Error: {e}")

print("Library status:", library)