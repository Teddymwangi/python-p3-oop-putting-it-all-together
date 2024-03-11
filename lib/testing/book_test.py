import pytest
from lib.book import Book

def test_book_initialization():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    assert book.title == "The Great Gatsby"
    assert book.author == "F. Scott Fitzgerald"
    assert book.pages == 180

def test_book_turn_page():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    book.turn_page()
    assert book.current_page == 2