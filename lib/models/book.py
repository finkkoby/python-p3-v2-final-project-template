from .author import Author
from .__init__ import CONN, CURSOR

class Book:

    all = []

    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author
    
    def __repr__(self):
        return f'<Book: {self.title}, {self.author}, {self.pages}>'
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError('Title must be a string')
        if len(title) < 3:
            raise ValueError('Title must be at least 3 characters')
        self._title = title

    @property
    def pages(self):
        return self._pages
    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError('Pages must be an integer')
        if pages < 1:
            raise ValueError('Pages must be at least 1')
        self._pages = pages
    
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError('Author must be an instance of the Author class')
        if len(author) < 3:
            raise ValueError('Author must be at least 3 characters')
        self._author = author