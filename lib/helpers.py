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
        print(f"\nFetching author info...")
        if isinstance(author, Author):
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
            else:
                print("Invalid input")
            
def find_author_by_id():
    while True:
        _id = input('Enter author id: ')
        author = Author.find_by_id(_id)
        print(f"\nFetching author info...")
        if isinstance(author, Author):
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
            else:
                print("Invalid input")

def create_author():
    while True:
        first_name = input('Enter author FIRST name: ')
        last_name = input('Enter author LAST name: ')
        check_author = Author.find_by_name(first_name, last_name)
        if isinstance(check_author, Author):
            print("\nWe already have '{last_name}, {first_name}' in our records.")
            answer = input("\nTry again? Y / N >> ")
            if answer == "Y":
                pass
            elif answer == "N":
                return
            else:
                print("Invalid input")
        else:
            check_input = input(f'\nCreate "{last_name}, {first_name}"? Y / N >> ')
            if check_input == "Y":
                author = Author.create(first_name, last_name)
                print(f"\nAuthor '{last_name}, {first_name}' created!")
                return
            elif check_input == "N":
                pass

def update_author():
    while True:
        _id = input('Enter author id: ')
        author = Author.find_by_id(_id)
        if isinstance(author, Author):
            first_name = input('Enter author FIRST name: ')
            last_name = input('Enter author LAST name: ')
            if first_name != '':
                author.first_name = first_name
            if last_name != '':
                author.last_name = last_name
            author.update()
            print(f"\n'{author.last_name}, {author.first_name}' updated!")
            return
        else:
            print("\nI can't find an author with that id.\n")
            answer = input("Try again? Y / N >> ")
            if answer == "Y":
                pass
            elif answer == "N":
                return
            else:
                print("Invalid input")

def delete_author():
    while True:
        _id = input('Enter author id: ')
        author = Author.find_by_id(_id)
        if isinstance(author, Author):
            answer = input(f"\nDelete '{author.last_name}, {author.first_name}'? Y / N >> ")
            if answer == "Y":
                author.delete()
                print(f"\n'{author.last_name}, {author.first_name}' deleted.")
                return
            else:
                answer = input("Try again? Y / N >> ")
                if answer == "Y":
                    pass
                elif answer == "N":
                    return
                else:
                    print("Invalid input")
        else:
            print("\nI can't find an author with that id.\n")
            answer = input("Try again? Y / N >> ")
            if answer == "Y":
                pass
            elif answer == "N":
                return
            else:
                print("Invalid input")

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
            else:
                print("Invalid input")


def find_book_by_id():
    _id = input('Enter book id: ')
    book = Book.find_by_id(_id)
    print("\nLet me grab that for you...\n")
    if isinstance(book, Book):
        author = Author.find_by_id(book.author_id)
        print(f"-- '{book.title}', {author.first_name} {author.last_name}, {book.pages} pages")
        return
    else:
        print(f"Looks like we don't have a book with that id\n")
        answer = input("Try again? Y / N >> ")
        if answer == "Y":
            pass
        elif answer == "N":
            return
        else:
            print("Invalid input")

        
        
def create_book():
    while True:
        title = input('Enter book title: ')
        pages = input('Enter number of pages in book: ')
        author_id = input('Enter author id: ')
        check_author = Author.find_by_id(int(author_id))
        check_book = Book.find_by_title(title)
        if isinstance(check_author, Author) and not isinstance(check_book, Book):
            check_input = input(f'\nCreate -- "{title}" by {check_author.first_name} {check_author.last_name}, {pages} pages -- ? Y / N >> ')
            if check_input == "Y":
                book = Book.create(title, int(pages), int(author_id))
                print(f"\n-- '{book.title}' by {check_author.first_name} {check_author.last_name}, {book.pages} pages -- created!")
                return
            elif check_input == "N":
                answer = input("Try again? Y / N >> ")
                if answer == "Y":
                    pass
                elif answer == "N":
                    return
                else:
                    print("Invalid input")
        elif not isinstance(check_author, Author):
            print("\nLooks like we don't have an author with that id.")
            answer = input("Would you like to create a new author? Y / N >> ")
            if answer == "Y":
                create_author()
            elif answer == "N":
                answer = input("Try again? Y / N >> ")
                if answer == "Y":
                    pass
                elif answer == "N":
                    return
                else:
                    print("Invalid input")
            else:
                print("Invalid input")
        elif isinstance(check_book, Book):
            print('\nLooks like we already have a book with that title.\n')
            answer = input("Try again? Y / N >> ")
            if answer == "Y":
                pass
            elif answer == "N":
                return
            else:
                print("Invalid input")
        else:
            print('\nOops! Something went wrong.\n')
            answer = input("Try again? Y / N >> ")
            if answer == "Y":
                pass
            elif answer == "N":
                return
            else:
                print("Invalid input")
    
def update_book():
    while True:
        _id = input('Enter book id: ')
        book = Book.find_by_id(_id)
        if isinstance(book, Book):
            title = input('Enter book title: ')
            pages = input('Enter number of pages in book: ')
            author_id = input('Enter author id: ')
            if title != '':
                book.title = title
            if pages != '':
                book.pages = pages
            if author_id != '':
                book.author_id = author_id
            book.update()
            print(f"\n-- '{book.title}', {book.pages} pages -- updated!")
            return
        else:
            print("\nI can't find a book with that id.\n")
            answer = input("Try again? Y / N >> ")
            if answer == "Y":
                pass
            elif answer == "N":
                return
            else:
                print("Invalid input")

def delete_book():
    while True:
        _id = input('Enter book id: ')
        book = Book.find_by_id(_id)
        if isinstance(book, Book):
            answer = input(f"\nDelete -- '{book.title}', {book.pages} pages -- ? Y / N >> ")
            if answer == "Y":
                book.delete()
                print(f"\n-- '{book.title}', {book.pages} pages -- deleted.")
                return
            else:
                answer = input("Try again? Y / N >> ")
                if answer == "Y":
                    pass
                elif answer == "N":
                    return
                else:
                    print("Invalid input")
        else:
            print("\nI can't find a book with that id.\n")
            answer = input("Try again? Y / N >> ")
            if answer == "Y":
                pass
            elif answer == "N":
                return
            else:
                print("Invalid input")

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