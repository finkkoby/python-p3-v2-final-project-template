# lib/helpers.py
from models.author import Author
from models.book import Book
from models.__init__ import CONN, CURSOR
import ipdb

def list_authors():
    authors = Author.get_all()
    for author in authors:
        print(author)

def find_author_by_name():
    pass
def find_author_by_id():
    pass
def create_author():
    pass
def update_author():
    pass
def delete_author():
    pass

def list_books():
    pass
def find_book_by_name():
    pass
def find_book_by_id():
    pass
def create_book():
    pass
def update_book():
    pass
def delete_book():
    pass

def list_author_books():
    pass


def exit_program():
    print("Goodbye!")
    exit()
