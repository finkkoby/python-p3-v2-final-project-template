# Welcome to my little library!

This CLI program is meant to replicate a little library of your very own. In it,
you are able to view books by title, or by author. You can check out a book (delete)
or even add a new book to your little library. This CLI also gives you the ability to
update any of the books or authors as well. Use this to keep track of your own reading
or anybooks you wish to read. It is very easy to read and use, even if you don't have
a ton of experience with command line or terminal!


## lib/cli.py

#### main()
This function prints the header and loops the **main_menu** function to keep the user
in the program.

#### main_menu()
This function provides the input field to allow the user to enter the library, either
by BOOK TITLE or by AUTHOR. If they input '1', the **book_menu** function is called,
and the **author_menu** function is called if they input '2' as their answer. Otherwise,
invalid input will be printed to the screen, and **main_menu** will be called again in
our **main** function.

#### book_menu() and author_menu()
These functions print a header to the screen to help break up the console output and make
it easier to understand. It then prints a header message, assuming no argument is passed
on the function call, and calls our next two functions. The optional argument is included
so that this function can be resued without the header messages, in case where it may
be redundant.

#### bookshelf_display() and author_display()
These functions are what prints our books or our authors to the screen. They also print the
next set of menu options to move forward or back in the program.

#### book_show_more() and author_show_more()
These functions allow for input based on the items and menu options provided in 
**bookshelf_display** and **author_display**. The display functions attach a number to each
book/author, to allow the user to select one and see more. The input of this function will
first check to see if the user input is an integer using the **check_for_int** functions. If
the user input is an integer, the function will return the book or author the user requested,
or it will return false if it is not an integer, or if the integer entered was invalid. Any
other user input will either redirect the user to different function call, or it will print
the invalid input message and loop back to allow for another input.

#### check_for_int()
There is a version of this function for a book and an author. The functions use try/except to
try and turn the string input into an integer and then retrieve the corresponding book/author
and return that object. If it is unable to do either of those things, it will return false.

#### book_actions() and author_actions()
These functions are called when a book or an author is selected by the user. These provide
more options for the user to modify the book/author as well as go to a different 'page'.
These also allow for input to select from the printed options.


## lib/helpers.py

#### list_books() and list_authors()
These function use the respective class method **get_all** to get the list of items to display
and prints each one to the screen.

#### find_book_by_id() and find_author_by_id()
These allow the CLI access to the respective class method of the same name.

#### create_book() and create_author()
These functions allow you to create a new book or author. They utilize the other helper functions
to obtain the necessary user input to do so. Both functions check to see if the title or author
name already exists, and if it does, it prints shows the invalid input message and asks the user if 
they wish to try again (see below).

#### update_book() and update_author()
These functions allow you to update an existing book or author. They utilize the other helper functions
to obtain the necessary user input to do so, the same used for creating new items. They then call
the instance method to update the database as well as the object in memory.

#### delete_book() and delete_author()
These functions allow you to delete an existing book or author. In the case of books, since it is a 
library style program, this action is referred to as 'checking out' a book. Both functions remove 
the book and author from the database. In the case of authors, it will not let you delete an author
if there are still books on the shelf by that author.

#### select_book() and select_author()
These helper functions display the list of books or authors and then allows the user to input which
they would like to select. It then verifies that the input is a valid integer before fetching and 
returning the selected item.

#### collect_book_info() and collect_author_name()
These are used when updating or creating new items. Once these functions have the necessary valid 
input from the user, it will use the verify functions to allow the user to confirm what they input.

#### verify_book_info() and verify_author_name()
As noted with the above functions, these functions allow the user to verify the information they
put in before moving forward.

#### author_book_display()
This helper function displays a list of books by a given author. It also accounts for the case in
which there are no books on the shelf by a given author.

#### exit_program() and try_again()
Exit program is not accessible by the user, but it is provided for developers. The **try_again**
function is used in cases of invalid input by user, or if there is any kind of problem that 
occurred during user action. It asks the user if they want to try again, and returns a boolean
value indicating to the function that called it whether or not to break out of the loop.

## Models

I set up two standard classes, one for books and one for authors. They have your standard instance
methods to create, modify, or remove items from the database as well the necessary class methods
to handle the creation of the datatables and any requests made to the database.

## lib/debug.py

I included this for testing purposes as well as resetting the database and passing in some default
information to get started.