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
    Author.create("Leigh", "Bardugo")
    Author.create("Taylor Jenkins", "Reid")
    Author.create("Casey", "McQuiston")
    Author.create("Stephen", "King")
    Author.create("Sarah J.", "Maas")

    Book.drop_table()
    Book.create_table()
    Book.create("A Court of Thorns and Roses", 448, 5)
    Book.create("Maybe in Another Life", 352, 2)
    Book.create("Red, White and Royal Blue", 423, 3)
    Book.create("Ruin and Rising", 352, 1)
    Book.create("Seige and Storm", 496, 1)
    Book.create("Shadow and Bone", 358, 1)
    Book.create("The Seven Husbands of Evelyn Hugo", 400, 2)
    Book.create("The Shining", 447, 4)
    


    ipdb.set_trace()

debug()