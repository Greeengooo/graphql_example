from typing import List

import strawberry

from models import G_Book
from storage import get_all_books, get_by_isbn, get_by_year, get_by_author, put_book_to_storage


@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> List[G_Book]:
        return get_all_books()

    @strawberry.field
    def book(self, isbn: int) -> G_Book:
        return get_by_isbn(isbn)

    @strawberry.field
    def book(self, year: int) -> List[G_Book]:
        return get_by_year(year)

    @strawberry.field
    def book(self, author: str) -> List[G_Book]:
        return get_by_author(author)


@strawberry.type
class Mutation:
    @strawberry.field
    def add_book(self, isbn: int, title: str, author: List[str], year: int) -> G_Book:
        book = G_Book(isbn=isbn, title=title, author=author, year=year)
        return put_book_to_storage(book)
