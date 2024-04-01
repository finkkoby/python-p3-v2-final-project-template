# lib/helpers.py
from models.author import Author
from models.book import Book
from models.__init__ import CONN, CURSOR
import ipdb

def list_authors():
    print("Fetching all artists..")
    authors = Author.get_all()
    for author in authors:
        print(f"-- {author.first_name} {author.last_name}")

def collect_author_name():
    while True:
        first_name = input('Enter author FIRST name: ')
        last_name = input('Enter author LAST name: ')
        check_input = input(f'Search for "{last_name}, {first_name}"? Y / N >> ')
        if check_input == "Y":
            return Author.find_by_name(first_name, last_name)
        elif check_input == "N":
            pass
        else:
            print("Invalid input")

def find_author_by_name():
    author = collect_author_name()
    print(f"Fetching author info...")
    print(f"\n{author.first_name} {author.last_name}\n")
    show_books(author)
    return
            
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

def list_author_books(author=None):
    if author is None:
        author = collect_author_name()
    books = [book for book in author.books() if len(author.books()) > 0]
    for book in books:
        print(f"\n'{book.title}', {book.pages} pages")



def exit_program():
    print("Goodbye!")
    exit()

def show_more():
    while True:
        answer = input("Anything else? Y / N >> ")
        if answer == "Y":
            return
        elif answer == "N":
            exit_program()
        else:
            print("Invalid input")

def show_books(author):
    while True:
        answer = input("Show books? Y / N >> ")
        if answer == "Y":
            list_author_books(author)
            return
        elif answer == "N":
            return
        else:
            print("Invalid input")
