import time
from helpers import (
    list_books,
    list_authors,
    create_author,
    create_book,
    update_author,
    update_book,
    delete_author,
    delete_book,
    find_book_by_id,
    find_author_by_id,
    author_book_display
)

def main():
    print("\n\n -<*==||  WELCOME TO MY BOOKSHELF  ||==*>- \n")
    while True:
        main_menu()

def main_menu():
    while True:
        answer = input('\nShow by (1) BOOK TITLE or by (2) AUTHOR? >> ')
        if answer == '1':
            book_menu()
            break
        elif answer == '2':
            author_menu()
            break
        else:
            print('\n ** Invalid input **')
            time.sleep(1)

# --- BOOK HOME MENU ---
def book_menu(display=True):
    print('\n\n <*- -=--  BOOKS  --=- -*> \n')
    if display:
        print("Here are all of the books that are available:\n")
        time.sleep(1)
    bookshelf_display()
    book_show_more()    

def bookshelf_display():
    list_books()
    time.sleep(1)
    print('\n(A) Add a book')
    print('(S) Show authors')
    print('(B) Back to menu')
    print(' ... or enter any number to take a book off the shelf!\n')

def book_show_more():
    while True:
        answer = input(f"\n  >> ")
        book = check_for_int_book(answer)
        if book:
            book_actions(book)
            break
        else:
            if answer.upper() == 'A':
                create_book()
                book_menu()
                break
            elif answer.upper() == 'S':
                author_menu()
                break
            elif answer.upper() == 'B':
                main_menu()
                break
            else:
                print("\n ** Invalid input **")
                time.sleep(1)

def check_for_int_book(string):
    try:
        _id = int(string)
        return find_book_by_id(_id)
    except:
        return False

def book_actions(book):
    print('\n\n <*- -=--  BOOKS  --=- -*> \n')
    author = find_author_by_id(book.author_id)
    print(f'->> {book.title}, {author.first_name} {author.last_name}, {book.pages} pages <<-')
    print("\n(U) Update book\n(C) Check out book\n(B) Back to books")
    while True:
        answer = input('\n  >> ')
        if answer.upper() == 'U':
            update_book(book)
            book_actions(book)
            break
        elif answer.upper() == 'C':
            delete_book(book, author)
            book_menu()
            break
        elif answer.upper() == 'B':
            book_menu()
            break
        else:
            print("\n ** Invalid input **")
            time.sleep(1)


# --- AUTHOR HOME MENU --- 
def author_menu(display=True):
    print('\n\n <*- -=--  AUTHORS  --=- -*> \n')
    if display:
        print("Here are the authors in our collection:\n")
        time.sleep(1)
    author_display()
    author_show_more()

def author_display():
    list_authors()
    time.sleep(1)
    print('\n(A) Add an author')
    print('(R) Remove an author')
    print('(S) Show books')
    print('(B) Back to menu')
    print(' ... or enter any number to show our books by that author!\n')

def author_show_more():
    while True:
        answer = input(f"\n  >> ")
        author = check_for_int_author(answer)
        if author:
            author_actions(author)
            break
        else:
            if answer.upper() == 'A':
                create_author()
                author_menu()
                break
            elif answer.upper() == 'R':
                delete_author()
                break
            elif answer.upper() == 'S':
                book_menu()
                break
            elif answer.upper() == 'B':
                main_menu()
                break
            else:
                print("\n ** Invalid input **")
                time.sleep(1)

def check_for_int_author(string):
    try:
        _id = int(string)
        return find_author_by_id(_id)
    except:
        return False

def author_actions(author):
    print('\n\n <*- -=--  AUTHORS  --=- -*> \n')
    print(f'{author.first_name} {author.last_name}\n')
    author_book_display(author)
    print("\n(U) Update author\n(A) Add book by author \n(B) Back to authors\n")
    while True:
        answer = input('  >> ')
        try:
            int(answer)
            book = find_book_by_id(answer)
            if book:
                book_actions(book)
                break
            else:
                print("\n ** Invalid input **")
                time.sleep(1)
        except:
            if answer.upper() == 'U':
                update_author(author)
                author_actions(author)
                break
            elif answer.upper() == 'A':
                create_book(author)
                author_actions(author)
                break
            elif answer.upper() == 'B':
                author_menu()
                break
            else:
                print("\n ** Invalid input **")
                time.sleep(1)

if __name__ == "__main__":
    main()
