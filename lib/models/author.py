from book import Book

class Author:

    all = []

    def __init__(self, name, books=[]):
        self.name = name
        self.books = books
    
    def __repr__(self):
        return f'<Author: {self.name}>'
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 2:
            raise ValueError("Name must be at least 2 characters long")
        self._name = name

    @property
    def books(self):
        return self._books
    @books.setter
    def books(self, books):
        if not isinstance(books, list):
            raise TypeError("Books must be a list")
        for book in books:
            if not isinstance(book, Book):
                raise TypeError("Books must be instances of the Book class")
        self._books = books

    