# lib/helpers.py
from models.author import Author
from models.book import Book
from models.__init__ import CONN, CURSOR
import ipdb

def list_authors():
    print("\nFetching all authors...\n")
    authors = Author.get_all()
    for i, author in enumerate(authors, start=1):
        print(f"{i}. {author.first_name} {author.last_name}")

def collect_author_name():
    while True:
        first_name = input('Enter author FIRST name: ')
        last_name = input('Enter author LAST name: ')
        check_input = input(f'Search for "{last_name}, {first_name}"? Y / N >> ')
        if check_input.upper() == "Y":
            return Author.find_by_name(first_name, last_name)
        elif check_input.upper() == "N":
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
            if answer.upper() == "Y":
                pass
            elif answer.upper() == "N":
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
            if answer.upper() == "Y":
                pass
            elif answer.upper() == "N":
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
            if answer.upper() == "Y":
                pass
            elif answer.upper() == "N":
                return
            else:
                print("Invalid input")
        else:
            check_input = input(f'\nCreate "{last_name}, {first_name}"? Y / N >> ')
            if check_input.upper() == "Y":
                author = Author.create(first_name, last_name)
                print(f"\nAuthor '{last_name}, {first_name}' created!")
                return author.id
            elif check_input.upper() == "N":
                pass

def update_author(_id):
    while True:
        author = Author.find_by_id(_id)
        first_name = input('Enter author FIRST name: ')
        last_name = input('Enter author LAST name: ')
        if first_name != '':
            author.first_name = first_name
        if last_name != '':
            author.last_name = last_name
        author.update()
        print(f"\n'{author.last_name}, {author.first_name}' updated!")
        return

def delete_author(_id=None):
    while True:
        if _id is None:
            _id = input("SELECT author from list:")
            author = Author.find_by_id(_id)
        else:
            author = Author.find_by_id(_id)
        if isinstance(author, Author):
            answer = input(f"\nDelete '{author.last_name}, {author.first_name}'? Y / N >> ")
            if answer.upper() == "Y":
                if len(author.books()) == 0:
                    author.delete()
                    print(f"\n'{author.last_name}, {author.first_name}' deleted.")
                    return
                else:
                    print(f"\n'{author.last_name}, {author.first_name}' can't be deleted.")
                    print('\nIt looks like we still have a few books by that author on the shelf.')
                    list_author_books(author)
                    answer = input("\nTry again? Y / N >> ")
                    if answer.upper() == "Y":
                        pass
                    elif answer.upper() == "N":
                        return
                    else:
                        print("Invalid input")
                        return
            elif answer.upper() == "N":
                return
            else:
                print("\nInvalid input")
        else:
            print("\nI can't find an author with that id.\n")
            answer = input("Try again? Y / N >> ")
            if answer.upper() == "Y":
                pass
            elif answer.upper() == "N":
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
            if answer.upper() == "Y":
                pass
            elif answer.upper() == "N":
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
        if answer.upper() == "Y":
            pass
        elif answer.upper() == "N":
            return
        else:
            print("Invalid input")

        
        
def create_book(_id=None):
    while True:
        title = input('Enter book title: ')
        pages = input('Enter number of pages in book: ')
        if _id is None:
            author_display(False)
            author_id = input('\nEnter author from list: ')
        else:
            author_id = _id
        if author_id == '+':
            author_id = create_author()
        elif author_id.upper() == 'B':
            back_to_menu()
        check_author = Author.find_by_id(int(author_id))
        if not isinstance(check_author, Author):
            print("\nInvalid input")
            answer = input("Would you like to create a new author? Y / N >> ")
            if answer == "Y":
                author_id = create_author()
                check_author = Author.find_by_id(author_id)
            elif answer.upper() == "N":
                answer = input("Try again? Y / N >> ")
                if answer.upper() == "Y":
                    pass
                elif answer.upper() == "N":
                    return
                else:
                    print("Invalid input")
            else:
                print("Invalid input")
        check_book = Book.find_by_title(title)
        if not isinstance(check_book, Book):
            check_input = input(f'\nReturn -- "{title}" by {check_author.first_name} {check_author.last_name}, {pages} pages -- ? Y / N >> ')
            if check_input.upper() == "Y":
                book = Book.create(title, int(pages), int(author_id))
                print(f"\n-- '{book.title}' by {check_author.first_name} {check_author.last_name}, {book.pages} pages -- returned!")
                return
            elif check_input.upper() == "N":
                answer = input("Try again? Y / N >> ")
                if answer.upper() == "Y":
                    pass
                elif answer.upper() == "N":
                    return
                else:
                    print("Invalid input")
        elif isinstance(check_book, Book):
            print('\nLooks like we already have a book with that title.\n')
            answer = input("Try again? Y / N >> ")
            if answer.upper() == "Y":
                pass
            elif answer.upper() == "N":
                return
            else:
                print("Invalid input")
        else:
            print('\nOops! Something went wrong.\n')
            answer = input("Try again? Y / N >> ")
            if answer.upper() == "Y":
                pass
            elif answer.upper() == "N":
                return
            else:
                print("Invalid input")
    
def update_book(_id):
    while True:
        book = Book.find_by_id(_id)
        title = input('Enter book title: ')
        pages = input('Enter number of pages in book: ')
        author_display(False)
        author_id = input('SELECT author from list: ')
        if title != '':
            book.title = title
        if pages != '':
            book.pages = int(pages)
        if author_id != '':
            book.author_id = int(author_id)
        book.update()
        author = Author.find_by_id(book.author_id)
        print(f"\n-- '{book.title}', {author.first_name} {author.last_name}, {book.pages} pages -- updated!")
        return

def delete_book(_id=None):
    while True:
        if _id is None:
            _id = input('\nSELECT book from list: ')
        book = Book.find_by_id(_id)
        answer = input(f"\nCheck out -- '{book.title}', {book.pages} pages -- ? Y / N >> ")
        if answer.upper() == "Y":
            book.delete()
            print(f"\n-- '{book.title}', {book.pages} pages -- checked out.")
            return
        elif answer.upper() == "N":
            return
        else:
            print("\nInvalid input")

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

def show_more(string):
    while True:
        answer = input(f"\n  >> ")
        if answer.upper() == 'Z':
            exit_program()
        elif answer.upper() == 'B':
            back_to_menu()
            return
        elif answer.upper() == 'L':
            type_menu(author_menu())
            return
        elif answer.upper() == 'R':
            create_book()
            type_menu(book_menu())
            return
        elif answer.upper() == 'C':
            delete_book()
            type_menu(book_menu())
            return
        elif answer.upper() == 'A':
            return author_menu()
        elif answer.upper() == 'S':
            return book_menu()

        elif answer == '+':
            create_author()
            type_menu(author_menu())
            return
        elif answer == '-':
            delete_author()
            type_menu(author_menu())
            return
        elif int(answer):
            if string == 'book':
                print('\n--------------------------------')
                book = Book.find_by_id(int(answer))
                if isinstance(book, Book):
                    author = Author.find_by_id(book.author_id)
                    print(f'{book.title}, {author.first_name} {author.last_name}, {book.pages} pages')
                    book_actions(book.id)
                    return
                else:
                    print("\nHmmm...I can't seem to find that one. Try again.\n")
            elif string == 'author':
                print('\n--------------------------------')
                author = Author.find_by_id(int(answer))
                if isinstance(author, Author):
                    print(f'{author.last_name}, {author.first_name}')
                    author_actions(author.id)
                    return
                else:
                    print("\nHmmm...I can't seem to find that one. Try again.\n")
        else:
            print("Invalid input")
        

def show_books(author):
    while True:
        answer = input("Show books? Y / N >> ")
        if answer.upper() == "Y":
            list_author_books(author)
            return
        elif answer.upper() == "N":
            return
        else:
            print("Invalid input")

def show_by():
    while True:
        answer = input('\nShow by (1) BOOK TITLE or by (2) AUTHOR? >> ')
        if answer == '1':
            book_menu()
            return
        elif answer == '2':
            author_menu()
            return
        else:
            print('Invalid input')

def book_menu(display=True):
    if display:
        bookshelf_display()
    else:
        print('\n(L) Back to books list\n')
    show_more('book')
    return

def author_menu(display=True):
    if display:
        author_display()
    show_more('author')
    return

def bookshelf_display(display=True):
    print('\n--------------------------------')
    print("Here are all of the books that are available:\n")
    for i, book in enumerate(Book.get_all(), start=1):
        author = Author.find_by_id(book.author_id)
        print(f'{i} -- {book.title}, {author.first_name} {author.last_name}, {book.pages} pages')
    if display:
        print('\n(R) Return a book')
        print('(C) Check out a book')
        print('(A) Show authors')
        print('(B) Back to menu\n')
        print('OR')
        print('\nEnter any number to take a book of the shelf!\n')

def author_display(display=True):
    print('\n--------------------------------')
    print("Here are the authors in our collection: \n")
    for i, author in enumerate(Author.get_all(), start=1):
        print(f'{i} -- {author.last_name}, {author.first_name}')
    if display:
        print('\n(+) Add an author')
        print('(-) Remove an author')
        print('(S) Show books')
        print('(B) Back to menu\n')

def book_actions(_id, display=False):
    while True:
        if display:
            print('\n--------------------------------')
            book = Book.find_by_id(_id)
            author = Author.find_by_id(book.author_id)
            print(f'{book.title}, {author.first_name} {author.last_name}, {book.pages} pages')
        print("\n(1) Update book\n(2) Check out book\n(3) Back to books\n")
        answer = input('>> ')
        if answer == '1':
            update_book(_id)
            book_actions(_id, True)
            return
        elif answer == '2':
            delete_book(_id)
            book_menu()
            return
        elif answer == '3':
            book_menu()
            return

def author_actions(_id, display=False):
    while True:
        if display:
            author = Author.find_by_id(_id)
            print('\n--------------------------------')
            print(f'{author.last_name}, {author.first_name}')
        print("\n(1) Update author\n(2) Show books by author\n(3) Return book by author \n(4) Back to authors\n")
        print('(B) Back to menu\n')
        answer = input('>> ')
        if answer == '1':
            update_author(_id)
            author_actions(_id, True)
            return
        elif answer == '2':
            author_book_display(Author.find_by_id(_id))
            return
        elif answer == '3':
            create_book(_id)
        elif answer == '4':
            answer = author_menu()
            author_actions(_id, True)
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

def main_menu():
    show_by()


def back_to_menu():
    main_menu()