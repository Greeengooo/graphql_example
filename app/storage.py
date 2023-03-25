from typing import Union

from models import Book, G_Book

books = [
    Book(isbn=20000, title="Мануальна праця", author=["Тарас Бахборич"], year=2021),
    Book(
        isbn=30000, title="Історія одного павіана", author=["Тарас Бахборич"], year=2023
    ),
    Book(isbn=40000, title="Німецька для чайників", author=["Транс Піфка"], year=2018),
    Book(
        isbn=50000,
        title="Трипільська культура",
        author=["Суісайд Леопрад", "Слік Тронов"],
        year=2021,
    ),
    Book(
        isbn=60000,
        title="Найгидкіші істоти Всесвіту",
        author=["Тарас Замзович"],
        year=2018,
    ),
]


def get_all_books():
    return books


def get_by_isbn(isbn: int):
    book = [book for book in books if book.isbn == isbn]
    return book if book else []


def get_by_year(year: int):
    result = [book for book in books if book.year == year]
    return result if result else []


def get_by_author(author: str):
    result = [book for book in books if author in book.author]
    return result if result else []


def put_book_to_storage(book: Union[Book, G_Book]):
    books.append(book)
    return book


# graphql
def check_condition(filter_data, storage_data):
    if type(storage_data) is list:
        return filter_data in storage_data
    else:
        return filter_data == storage_data


def get_book_by_filters(filters: dict):
    result = []
    for book in books:
        condition = [
            check_condition(filters[i], book.__dict__[i]) for i in filters if filters[i]
        ]
        if all(condition):
            result.append(book)
    return result
