from .author import Author
from .__init__ import CONN, CURSOR

class Book:

    all = {}

    def __init__(self, title, pages, author_id=None):
        self.title = title
        self.pages = pages
        self.author_id = author_id
    
    def __repr__(self):
        return f'<Book: {self.title}, {self.pages}, {self.author_id}>'
    

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
        if type(author_id) is int and isinstance(Author.find_by_id(author_id), Author):
            self._author_id = author_id
        else:
            raise ValueError(f"Author {author_id} not found")

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

    def update(self):
        # update db with object stored in memory
        sql = """
            UPDATE books
            SET title = ?, pages = ?, author_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.pages, self.author_id, self.id))
        CONN.commit()

    def delete(self):
        # remove self from db but keep stored in memory
        del Book.all[self.id]
        sql = """
            DELETE FROM books
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

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
    def create(cls, title, pages, author_id):
        new_book = Book(title, pages, author_id)
        new_book.save()
        return new_book

    @classmethod
    def instance_from_db(cls, row):
        # returns object that is an instance of the CLS at the ROW in the database
        book = cls.all.get(row[0])
        if book:
            book.title = row[1]
            book.pages = row[2]
            book.author_id = row[3]
        else:
            book = cls(row[1], row[2], row[3])
            book.id = row[0]
            cls.all[book.id] = book
        return book


    @classmethod
    def get_all(cls):
        # a list containing objects that are instances of CLS from db
        sql = """
            SELECT *
            FROM books
        """
        CURSOR.execute(sql)
        books = CURSOR.fetchall()
        return [cls.instance_from_db(book) for book in books]

    @classmethod
    def find_by_id(cls, book_id):
        # object that is an instance of CLS in db with ID = book_id
        book_id = str(book_id)
        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (book_id,)).fetchone()
        return cls.instance_from_db(row) if row else f"Book '{book_id}' not found"

    @classmethod
    def find_by_title(cls, title):
        # object that is an instance of CLS in db with TITLE = title
        sql = """
            SELECT *
            FROM books
            WHERE title = ?
        """
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else f"Book '{title}' not found"