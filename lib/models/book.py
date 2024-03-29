from .author import Author
from .__init__ import CONN, CURSOR

class Book:

    all = {}

    def __init__(self, title, pages, author_id=None):
        self.title = title
        self.pages = pages
        self.author_id = author_id
    
    def __repr__(self):
        return f'<Book: {self.title}, {self.author}, {self.pages}>'
    

# PROPERTIES !!!!!!    
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
    def author_id(self):
        return self._author_id
    @author_id.setter
    def author_id(self, author_id):
        pass
        # use find_by_id method from Author class

# INTANCE METHODS !!!!!!
    def save(self):
        sql = """
            INSERT INTO books (title, pages, author_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.pages, self.author_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

# CLASS METHODS !!!!!!
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY,
                title TEXT,
                pages INTEGER,
                author_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES authors(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        # returns object that is an instance of the CLS at the ROW in the database
        book = cls.all[row[0]]
        if book:
            book.title = row[1]
            book.pages = row[2]
            book.author_id = row[3]
            return book
        else:
            raise Exception(f"Book {row[1]} not found")

    @classmethod
    def get_all(cls):
        # a list containing objects that are instances of CLS from db
        pass

    @classmethod
    def find_by_id(cls, book_id):
        # object that is an instance of CLS in db with ID = book_id
        pass

    @classmethod
    def find_by_title(cls, title):
        # object that is an instance of CLS in db with TITLE = title
        pass