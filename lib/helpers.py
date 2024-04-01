# lib/helpers.py
from models.author import Author
from models.book import Book
from models.__init__ import CONN, CURSOR
import ipdb

def list_authors():
    print("\nFetching all authors...\n")
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
    while True:
        author = collect_author_name()
        if isinstance(author, Author):
            print(f"\nFetching author info...")
            print(f"\n{author.first_name} {author.last_name}\n")
            show_books(author)
            return
        else:
            print("\nI can't find an author with that name.\n")
            answer = input("Try again? Y / N >> ")
            if answer == "Y":
                pass
            elif answer == "N":
                return
            
def find_author_by_id():
    while True:
        _id = input('Enter author id: ')
        author = Author.find_by_id(_id)
        if isinstance(author, Author):
            print(f"\nFetching author info...")
            print(f"\n{author.first_name} {author.last_name}\n")
            show_books(author)
            return
        else:
            print("\nI can't find an author with that id.\n")
            answer = input("Try again? Y / N >> ")
            if answer == "Y":
                pass
            elif answer == "N":
                return

def create_author():
    pass
def update_author():
    pass
def delete_author():
    pass

def list_books():
    print("\nFetching all books...\n")
    books = Book.get_all()
    for book in books:
        author = Author.find_by_id(book.author_id)
        print(f"-- '{book.title}', {author.first_name} {author.last_name}, {book.pages} pages")
    
def find_book_by_name():
    while True:
        title = input('Enter book title: ')
        book = Book.find_by_title(title)
        print("\nLet me grab that for you...\n")
        if isinstance(book, Book):
            author = Author.find_by_id(book.author_id)
            print(f"-- '{book.title}', {author.first_name} {author.last_name}, {book.pages} pages")
            return
        else:
            print(f"Looks like we don't have '{title}'\n")
            answer = input("Try again? Y / N >> ")
            if answer == "Y":
                pass
            elif answer == "N":
                return


def find_book_by_id():
    _id = input('Enter book id: ')
    book = Book.find_by_id(_id)

    if isinstance(book, Book):
        print()
def create_book():
    pass
def update_book():
    pass
def delete_book():
    pass

def list_author_books(author=None):
    if author is None:
        author = collect_author_name()
    print("\nFetching books...\n")
    books = [book for book in author.books() if len(author.books()) > 0]
    for book in books:
        print(f"'{book.title}', {book.pages} pages")



def exit_program():
    print("Goodbye!")
    exit()

def show_more():
    while True:
        answer = input("\nAnything else? Y / N >> ")
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
