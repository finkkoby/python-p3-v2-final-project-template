
from helpers import (
    exit_program,
    list_authors,
    find_author_by_name,
    find_author_by_id,
    create_author,
    update_author,
    delete_author,
    list_books,
    find_book_by_name,
    find_book_by_id,
    create_book,
    update_book,
    delete_book,
    list_author_books,
    show_more,
    show_by,
    book_actions,
    author_actions,
    main_menu
)

def main():
    print(f"\nWelcome to my bookshelf!\n")
    while True:
        main_menu()




if __name__ == "__main__":
    main()
