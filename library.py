"""
TASK: Create a Library class.

Requirements:
1. The class should track available books (list).
2. Provide a method to add new books to the library.
3. Provide a method for users to borrow books.
   - Remove the borrowed book from available list.
   - Store borrowed books with user info.
4. Provide a method for returning borrowed books.
5. Provide a method to show all available books.

Example Usage:
    lib = Library()
    lib.add_book("Python 101")
    lib.add_book("Data Science Handbook")
    lib.borrow_book("Alice", "Python 101")
    print(lib.show_available_books())  # ["Data Science Handbook"]
    lib.return_book("Alice")
    print(lib.show_available_books())  # ["Data Science Handbook", "Python 101"]
"""
class Library:
    def __init__(self):
        self.library = []
        self.borrowed_books = {}
    def add(self, book_title):
        self.book_title = book_title
        if self.book_title in self.library:
            print(f"{self.book_title} already exist")
        else:
            self.library.append(self.book_title)
    def borrow(self, user, book_title):
        
        self.user_name = user
        self.book_title = book_title
        if self.book_title in self.library:
            self.library.remove(self.book_title)
            self.borrowed_books.update({self.user_name:self.book_title})
        else:
            print(f"{self.book_title} is not available")
    def return_book(self, user):
        self.user_name = user
        if self.user_name in self.borrowed_books:
            self.library.append(self.borrowed_books[self.user_name])
            self.borrowed_books.pop(self.user_name)
        else:
            print("User not found")

    def available_books(self):
        return self.library


lib = Library()
lib.add("Python 101")
lib.add("FastAPI 101")
lib.add("Flask 101")

print(lib.available_books())
lib.borrow("ban", "Python 101")
print(lib.borrowed_books)
lib.return_book("ban")
print(lib.available_books())