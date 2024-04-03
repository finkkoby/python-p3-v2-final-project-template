
from helpers import (
    book_menu,
    author_menu
)

def main():
    print(f"\nWelcome to my bookshelf!\n")
    while True:
        main_menu()

def show_by():
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

def main_menu():
    show_by()

def back_to_menu():
    main_menu()

if __name__ == "__main__":
    main()
