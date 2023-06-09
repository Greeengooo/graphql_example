from typing import List, Optional

import strawberry
from models import G_Book
from storage import get_all_books, get_book_by_filters, put_book_to_storage


@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> List[G_Book]:
        return get_all_books()

    @strawberry.field
    def book(
        self,
        isbn: Optional[int] = None,
        title: Optional[str] = None,
        year: Optional[int] = None,
        author: Optional[str] = None,
    ) -> List[G_Book]:
        filters = {"isbn": isbn, "title": title, "year": year, "author": author}
        return get_book_by_filters(filters)


@strawberry.type
class Mutation:
    @strawberry.field
    def add_book(self, isbn: int, title: str, author: List[str], year: int) -> G_Book:
        book = G_Book(isbn=isbn, title=title, author=author, year=year)
        return put_book_to_storage(book)
