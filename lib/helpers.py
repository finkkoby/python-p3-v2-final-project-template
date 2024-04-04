# lib/helpers.py
from models.author import Author
from models.book import Book
from models.__init__ import CONN, CURSOR
import ipdb
import time

def list_authors():
    authors = Author.get_all()
    for author in authors:
        print(f"{author.id} -- {author.first_name} {author.last_name}")

def find_author_by_id(_id):
    return Author.find_by_id(_id)

def create_author():
    flag = True
    while flag:
        print('\n\n <*- -=--  CREATE AN AUTHOR  --=- -*> \n')
        name = collect_author_name()
        author = Author.find_by_name(name[0], name[1])
        if author:
            print(f"\nWe already have '{author.last_name}, {author.first_name}' in our records.")
            time.sleep(1)
            flag = try_again()
        else:
            try:
                new_author = Author.create(name[0], name[1])
                print(f"\n-- '{new_author.last_name}, {new_author.first_name}' -- created!")
                time.sleep(1)
                return author
            except Exception as e:
                print(f'\n ** {e} **')
                time.sleep(1)
                flag = try_again()

def update_author(author):
    print('\n\n <*- -=--  UPDATE AN AUTHOR  --=- -*> \n')
    name = collect_author_name()
    author.first_name = name[0]
    author.last_name = name[1]
    author.update()
    print(f"\n-- '{author.last_name}, {author.first_name}' -- updated!")
    time.sleep(1)

def delete_author():
    flag = True
    while flag:
        print('\n\n <*- -=--  DELETE AN AUTHOR  --=- -*> \n')
        author = select_author()
        answer = input(f"\nDelete '{author.last_name}, {author.first_name}'? Y / N >> ")
        if answer.upper() == "Y":
            if len(author.books()) == 0:
                author.delete()
                print(f"\n'{author.last_name}, {author.first_name}' deleted.")
                time.sleep(1)
                flag = False
            else:
                print(f"\n'{author.last_name}, {author.first_name}' can't be deleted.")
                print('\nIt looks like we still have a few books by that author on the shelf.')
                author_book_display(author)
                flag = try_again()
        elif answer.upper() == "N":
            flag = try_again()
        else:
            print("\n ** Invalid input **")
            time.sleep(1)

def select_author():
    print('\n\\\ Authors')
    list_authors()
    while True:
        _id = input("\n\\\ SELECT author from list -=> ")
        try:
            _id = int(_id)
            author = Author.find_by_id(_id)
            return author
        except:
            print('\n ** Invalid input **')
            time.sleep(1)

def collect_author_name():
    flag = True
    while flag:
        first_name = input('\\\ Enter author FIRST name: ')
        last_name = input('\\\ Enter author LAST name: ')
        flag = verify_author_name(first_name, last_name)
    return [first_name, last_name]

def verify_author_name(first_name, last_name):
    while True:
        check_input = input(f'\n "{last_name}, {first_name}"? Y / N >> ')
        if check_input.upper() == "Y":
            return False
        elif check_input.upper() == "N":
            return True
        else:
            print("\n ** Invalid input **")
            time.sleep(1)

def list_books(books=None):
    if not books:
        books = Book.get_all()
    for book in books:
        author = Author.find_by_id(book.author_id)
        print(f" {book.id} -- '{book.title}', {author.first_name} {author.last_name}, {book.pages} pages")     

def find_book_by_id(_id):
    return Book.find_by_id(_id)

def create_book(author=None):
    flag = True
    while flag:
        print('\n\n <*- -=--  ADD A BOOK  --=- -*> \n')
        info = collect_book_info(author)
        book = Book.find_by_title(info[0])
        if book:
            print('\nLooks like we already have a book with that title.\n')
            flag = try_again()
        else:
            try:
                book = Book.create(info[0], info[1], info[2].id)
                print(f"\n-- '{book.title}' by {info[2].first_name} {info[2].last_name}, {book.pages} pages -- created!")
                Book.update_id()
                time.sleep(1)
                flag = False
            except Exception as e:
                print(f'\n ** {e} **')
                time.sleep(1)
                flag = try_again()
    
def update_book(book):
    print('\n\n <*- -=--  UPDATE A BOOK  --=- -*> \n')
    flag = True
    while flag:
        info = collect_book_info()
        try:
            book.title = info[0]
            book.pages = info[1]
            book.author_id = info[2].id
            book.update()
            print(f"\n-- '{book.title}', {info[2].first_name} {info[2].last_name}, {book.pages} pages -- updated!")
            time.sleep(1)
            flag = False
        except Exception as e:
            print(f'\n ** {e} **')
            time.sleep(1)
            flag = try_again()

def delete_book(book=None, author=None):
    flag = True
    while flag:
        print('\n\n <*- -=--  CHECK OUT A BOOK  --=- -*> \n')
        if not book and not author:
            book = select_book()
            author = find_author_by_id(book.author_id)
        print(f'->> {book.title}, {author.first_name} {author.last_name}, {book.pages} pages <<-')
        answer = input(f"\nCheck out -- '{book.title}', {book.pages} pages -- ? Y / N >> ")
        if answer.upper() == "Y":
            book.delete()
            print(f"\n-- '{book.title}', {book.pages} pages -- checked out.")
            Book.update_id()
            time.sleep(1)
            flag = False
        elif answer.upper() == "N":
            flag = False
        else:
            print("\n ** Invalid input **")
            time.sleep(1)

def select_book():
    list_books()
    while True:
        _id = input('\n\\\ SELECT book from list -=> ')
        try:
            _id = int(_id)
            book = Book.find_by_id(_id)
            return book
        except:
            print('\n ** Invalid input **')
            time.sleep(1)

def collect_book_info(author=None):
    flag = True
    while flag:
        title = input('\\\ Enter book title -=> ')
        while True:
            try:
                pages = int(input('\\\ Enter number of pages in book -=> '))
                break
            except:
                print('\n ** Invalid input **\n')
                time.sleep(1)
        if not author:
            author = select_author()
        flag = verify_book_info(title, pages, author)
    return[title, pages, author]

def verify_book_info(title, pages, author):
    while True:
        check_input = input(f'\n "{title}" by {author.first_name} {author.last_name}, {pages} pages -- ? Y / N >> ')
        if check_input.upper() == "Y":
            return False
        elif check_input.upper() == "N":
            return True
        else:
            print("\n ** Invalid input **")
            time.sleep(1)

def exit_program():
    print("\n --  Goodbye!\n")
    exit()
 
def author_book_display(author):
    books = author.books()
    if len(books) == 0:
        print("\nLooks like we don't have any books by this author.\n")
        return
    else:
        list_books(books)

def try_again():
    while True:
        answer = input("\nTry again? Y / N >> ")
        if answer.upper() == "Y":
            return True
        elif answer.upper() == "N":
            return False
        else:
            print("\n ** Invalid input **")
            time.sleep(1)