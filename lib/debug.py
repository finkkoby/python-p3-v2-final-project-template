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
    Book.drop_table()
    Book.create_table()
    ipdb.set_trace()

debug()