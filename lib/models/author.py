from .__init__ import CONN, CURSOR

class Author:

    all = {}

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return f'<Author: {self.last_name}, {self.first_name}>'
    
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise TypeError("First name must be a string")
        if len(first_name) < 1:
            raise ValueError("First name must be at least 1 character long")
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str):
            raise TypeError("Last name must be a string")
        if len(last_name) < 1:
            raise ValueError("Last name must be at least 1 character long")
        self._last_name = last_name


# INSTANCE METHODS !!!!!!
    def save(self):
        sql = """
            INSERT INTO authors (first_name, last_name)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.first_name, self.last_name))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        # update db with object stored in memory
        sql = """
            UPDATE authors
            SET first_name = ?, last_name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.first_name, self.last_name))
        CONN.commit()
        print(f"Database updated: {self}")

    def delete(self):
        # remove self from db but keep stored in memory
        del Author.all[self.id]
        sql = """
            DELETE FROM authors
            WHERE id = ? 
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        print(f"Row deleted, object still stored in memory")


# CLASS METHODS !!!!!!
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS authors(
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS authors
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, first_name, last_name):
        new_author = Author(first_name, last_name)
        new_author.save()
        return new_author
    
    @classmethod
    def instance_from_db(cls, row):
        # returns object that is an instance of the CLS at the ROW in the database
        author = cls.all[row[0]]
        if author:
            author.first_name = row[1]
            author.last_name = row[2]
            return author
        else:
            raise Exception(f"Author {row} not found")

    @classmethod
    def get_all(cls):
        # a list containing objects that are instances of CLS from db
        sql = """
            SELECT *
            FROM authors
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, author_id):
        # object that is an instance of CLS in db with ID = author_id
        sql = """
            SELECT *
            FROM authors
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (author_id,)).fetchone()
        return cls.instance_from_db(row) if row else Exception(f'Author {author_id} not found')

    @classmethod
    def find_by_name(cls, first_name, last_name):
        # object that is an instance of CLS in db with matching first and last name
        sql = """
            SELECT *
            FROM authors
            WHERE first_name, last_name = (?, ?)
        """
        row = CURSOR.execute(sql, (first_name, last_name)).fetchone()
        return cls.instance_from_db(row) if row else Exception('Author "{last_name}, {first_name}" not found')