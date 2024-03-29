#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.book import Book

import sqlite3
import ipdb

def debug():
    Author.drop_table()
    Author.create_table()
    author_1 = Author.create("Leigh", "Bardugo")
    author_2 = Author.create("Taylor Jenkins", "Reid")

    Book.drop_table()
    Book.create_table()
    book_1 = Book.create("Shadow and Bone", 358, 1)
    book_2 = Book.create("Seige and Storm", 496, 1)
    book_3 = Book.create("The Seven Husbands of Evelyn Hugo", 400, 2)
    book_4 = Book.create("Maybe in Another Life", 352, 2)


    ipdb.set_trace()

debug()