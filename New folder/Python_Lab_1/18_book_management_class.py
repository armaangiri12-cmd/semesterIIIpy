# Creates book objects and demonstrates borrowing and returning a book.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print('"' + self.title + '" is already borrowed.')
        else:
            self.is_borrowed = True
            print('"' + self.title + '" has been borrowed.')

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print('"' + self.title + '" has been returned.')
        else:
            print('"' + self.title + '" was not borrowed.')

    def display_details(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(self.title + " by " + self.author + " - " + status)


books = [
    Book("Python Basics", "R. Sharma"),
    Book("Learning to Code", "A. Patel"),
]

for book in books:
    book.display_details()

books[0].borrow()
books[0].display_details()
books[0].return_book()
