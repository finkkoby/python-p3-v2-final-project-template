# lib/helpers.py
from models.author import Author
from models.book import Book
from models.__init__ import CONN, CURSOR
import ipdb
import time

def list_authors():
    authors = Author.get_all()
    for i, author in enumerate(authors, start=1):
        print(f"{i}. {author.first_name} {author.last_name}")

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
            new_author = Author.create(name[0], name[1])
            print(f"\nAuthor '{new_author.last_name}, {new_author.first_name}' created!")
            time.sleep(1)
            return author

def update_author(author):
    print('\n\n <*- -=--  UPDATE AN AUTHOR  --=- -*> \n')
    name = collect_author_name()
    author.first_name = name[0]
    author.last_name = name[1]
    author.update()
    print(f"\n'{author.last_name}, {author.first_name}' updated!")
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
                list_author_books(author)
                flag = try_again()
        elif answer.upper() == "N":
            flag = try_again()
        else:
            print("\n ** Invalid input **")

def select_author():
    author_display(False)
    while True:
        _id = input("\nSELECT author from list: ")
        try:
            _id = int(_id)
            author = Author.find_by_id(_id)
            return author
        except:
            print('\n ** Invalid input **')

def collect_author_name():
    flag = True
    while flag:
        first_name = input('Enter author FIRST name: ')
        last_name = input('Enter author LAST name: ')
        flag = verify_author_name(first_name, last_name)
    return [first_name, last_name]

def verify_author_name(first_name, last_name):
    while True:
        check_input = input(f' "{last_name}, {first_name}"? Y / N >> ')
        if check_input.upper() == "Y":
            return False
        elif check_input.upper() == "N":
            return True
        else:
            print("\n ** Invalid input **")

def list_books():
    books = Book.get_all()
    for i, book in enumerate(books, start=1):
        author = Author.find_by_id(book.author_id)
        print(f" {i} -- '{book.title}', {author.first_name} {author.last_name}, {book.pages} pages")     
    
def create_book(author=None):
    print('\n\n <*- -=--  ADD A BOOK  --=- -*> \n')
    flag = True
    while flag:
        info = collect_book_info(author)
        book = Book.find_by_title(info[0])
        if book:
            print('\nLooks like we already have a book with that title.\n')
            flag = try_again()
        else:
            book = Book.create(info[0], info[1], info[2])
            print(f"\n-- '{book.title}' by {info[2].first_name} {info[2].last_name}, {book.pages} pages -- created!")
            time.sleep(1)
            flag = False
    
def update_book(book):
    print('\n\n <*- -=--  UPDATE A BOOK  --=- -*> \n')
    info = collect_book_info()
    book.title = info[0]
    book.pages = info[1]
    book.author = info[2]
    book.update()
    print(f"\n-- '{book.title}', {info[2].first_name} {info[2].last_name}, {book.pages} pages -- updated!")
    time.sleep(1)

def delete_book(book=None):
    print('\n\n <*- -=--  CHECK OUT A BOOK  --=- -*> \n')
    flag = True
    while flag:
        if not book:
            book = select_book()
        answer = input(f"\nCheck out -- '{book.title}', {book.pages} pages -- ? Y / N >> ")
        if answer.upper() == "Y":
            book.delete()
            print(f"\n-- '{book.title}', {book.pages} pages -- checked out.")
            time.sleep(1)
            flag = False
        elif answer.upper() == "N":
            flag = False
        else:
            print("\n ** Invalid input **")

def collect_book_info(book=None):
    flag = True
    while flag:
        title = input('Enter book title: ')
        while True:
            try:
                pages = int(input('Enter number of pages in book: '))
                break
            except:
                print('\n ** Invalid input **')
        if not author:
            author = select_author()
        flag = verify_book_info(title, pages, author)
    return[title, pages, author]

def select_book():
    bookshelf_display(False)
    while True:
        _id = input('\nSELECT book from list: ')
        try:
            _id = int(_id)
            book = Book.find_by_id(_id)
            return book
        except:
            print('\n ** Invalid input **')

def verify_book_info(title, pages, author):
    while True:
        check_input = input(f'\n "{title}" by {author.first_name} {author.last_name}, {pages} pages -- ? Y / N >> ')
        if check_input.upper() == "Y":
            return False
        elif check_input.upper() == "N":
            return True
        else:
            print("\n ** Invalid input **")
        

def list_author_books(author=None):
    if not author:
        author = collect_author_name()
    books = [book for book in author.books() if len(author.books()) > 0]
    for book in books:
        print(f"'{book.title}', {book.pages} pages")



def exit_program():
    print("Goodbye!")
    exit()

def show_more(string):
    while True:
        answer = input(f"\n  >> ")
        if answer.upper() == 'Z':
            exit_program()
        elif answer.upper() == 'B':
            back_to_menu()
            return
        elif answer.upper() == 'L':
            author_menu()
            return
        elif answer.upper() == 'R':
            create_book()
            book_menu()
            return
        elif answer.upper() == 'C':
            delete_book()
            book_menu()
            return
        elif answer.upper() == 'A':
            return author_menu()
        elif answer.upper() == 'S':
            return book_menu()
        elif answer == '+':
            create_author()
            author_menu()
            return
        elif answer == '-':
            delete_author()
            author_menu()
            return
        elif int(answer):
            if string == 'book':
                print('\n--------------------------------')
                book = Book.find_by_id(int(answer))
                if isinstance(book, Book):
                    author = Author.find_by_id(book.author_id)
                    print(f'{book.title}, {author.first_name} {author.last_name}, {book.pages} pages')
                    book_actions(book)
                    return
                else:
                    print("\nHmmm...I can't seem to find that one. Try again.\n")
            elif string == 'author':
                print('\n--------------------------------')
                author = Author.find_by_id(int(answer))
                if isinstance(author, Author):
                    print(f'{author.last_name}, {author.first_name}')
                    author_actions(author)
                    return
                else:
                    print("\nHmmm...I can't seem to find that one. Try again.\n")
        else:
            print("\n ** Invalid input **")
        

def show_books(author):
    while True:
        answer = input("Show books? Y / N >> ")
        if answer.upper() == "Y":
            list_author_books(author)
            return
        elif answer.upper() == "N":
            return
        else:
            print("\n ** Invalid input **")

def book_menu(display=True):
    print('\n\n <*- -=--  BOOKS  --=- -*> \n')
    print("Here are all of the books that are available:\n")
    if display:
        bookshelf_display()
    else:
        print('\n(L) Back to books list\n')
    show_more('book')
    return

def author_menu(display=True):
    if display:
        print('\n\n <*- -=--  AUTHORS  --=- -*> \n')
        print("Here are the authors in our collection:\n")
        author_display()
    show_more('author')
    return

def bookshelf_display(display=True):
    list_books()
    if display:
        print('\n(R) Add a book')
        print('(C) Check out a book')
        print('(A) Show authors')
        print('(B) Back to menu\n')
        print('OR')
        print('\nEnter any number to take a book off the shelf!\n')

def author_display(display=True):
    list_authors()
    if display:
        print('\n(+) Add an author')
        print('(-) Remove an author')
        print('(S) Show books')
        print('(B) Back to menu\n')

def book_actions(book, display=False):
    while True:
        if display:
            print('\n--------------------------------')
            author = Author.find_by_id(book.author_id)
            print(f'{book.title}, {author.first_name} {author.last_name}, {book.pages} pages')
        print("\n(1) Update book\n(2) Check out book\n(3) Back to books\n")
        answer = input('>> ')
        if answer == '1':
            update_book(book)
            book_actions(book, True)
            return
        elif answer == '2':
            delete_book(book)
            book_menu()
            return
        elif answer == '3':
            book_menu()
            return

def author_actions(author, display=False):
    while True:
        if display:
            print('\n--------------------------------')
            print(f'{author.last_name}, {author.first_name}')
        print("\n(1) Update author\n(2) Show books by author\n(3) Add book by author \n(4) Back to authors\n")
        print('(B) Back to menu\n')
        answer = input('>> ')
        if answer == '1':
            update_author(author)
            author_actions(author, True)
            return
        elif answer == '2':
            author_book_display(author)
            return
        elif answer == '3':
            create_book(author)
        elif answer == '4':
            answer = author_menu()
            author_actions(author, True)
            return
        elif answer.upper() == 'B':
            back_to_menu()
    
def author_book_display(author):
    books = author.books()
    if len(books) == 0:
        print('\n--------------------------------')
        print("\nLooks like we don't have any books by this author.\n")
        return
    else:
        print('\n--------------------------------')
        print("\nHere are the books by this author:\n")
        for book in books:
            author = Author.find_by_id(book.author_id)
            print(f'{book.id} -- {book.title}, {author.first_name} {author.last_name}, {book.pages} pages')
        book_menu(False)

def try_again():
    while True:
        answer = input("\nTry again? Y / N >> ")
        if answer.upper() == "Y":
            return True
        elif answer.upper() == "N":
            return False
        else:
            print("\n ** Invalid input **")