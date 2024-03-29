#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.book import Book

def seed_database():
    Author.drop_table()
    Author.create_table()
    author_1 = Author.create("Leigh", "Bardugo")
    author_2 = Author.create("Taylor Jenkins", "Reid")

    Book.drop_table()
    Book.create_table()
    Book.create("Shadow and Bone", 358, author_1.id)
    Book.create("Seige and Storm", 496, author_1.id)
    Book.create("The Seven Husbands of Evelyn Hugo", 400, author_2.id)
    Book.create("Maybe in Another Life", 352, author_2.id)

seed_database()
print("Database seeded")