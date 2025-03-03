class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
	self.borrow_books = []
    # Ajouter les méthodes ici

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)

    def remove_book(self, title):
        for book in self.books:
            if title == book.title:
                self.books.remove(book)
                print(f"Le livre : {title}, a été retiré de la base de données.")
                break

    def borrow_book(self, title):
        for book in self.books:
            if title == book.title:
                self.remove_book(title)
                self.borrowed_books.append(book)
                print(f"Vous avez emprunté : {title}")
                break
            else:
                print("Le livre ne figure pas dans la base de données.")

    def return_book(self, title):
        for book in self.borrowed_books:
            if book.title == title:
                self.borrowed_books.remove(book)
                self.add_book(book.title, book.author, book.year)
                break

    def available_books(self):
        return self.books

    def borrowed_books(self):
        return self.borrowed_books


Livre1 = Book("Harry Potter", "JK Rolling", 1998)
Library_Lyon = Library()
Library_Lyon.books = []
Library_Lyon.add_book("Harry Potter","JK Rolling", 1998)

Library_Lyon.borrow_book("Harry Potter")
print(Library_Lyon.books)
print(Library_Lyon.borrowed_books)
print(Library_Lyon.return_book("Harry Potter"))
print(Library_Lyon.borrowed_books)
print(Library_Lyon.books)
