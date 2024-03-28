import sqlite3

CONN = sqlite3.connect('bookshelf.db')
CURSOR = CONN.cursor()
