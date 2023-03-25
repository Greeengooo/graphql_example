from typing import Union

from models import Book, G_Book

books = [
    Book(isbn=12345, title="Test1", author=["John Doe"], year=2021),
    Book(isbn=54321, title="Test2", author=["John Doe"], year=2022),
    Book(isbn=13578, title="Test3", author=["John Doe", "Ping Pong"], year=2023),
]


def get_all_books():
    return books


def get_by_isbn(isbn: int):
    book = [book for book in books if book.isbn == isbn]
    return book[0] if book else None


def get_by_year(year: int):
    result = [book for book in books if book.year == year]
    return result


def get_by_author(author: str):
    result = [book for book in books if author in book.author]
    return result


def put_book_to_storage(book: Union[Book, G_Book]):
    books.append(book)
    return book
