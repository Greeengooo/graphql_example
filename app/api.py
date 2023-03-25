import strawberry
from fastapi import FastAPI
from graphql_schema import Mutation, Query
from models import Book
from storage import (
    get_all_books,
    get_by_author,
    get_by_isbn,
    get_by_year,
    put_book_to_storage,
)
from strawberry.fastapi import GraphQLRouter

app = FastAPI()


# graphql endpoint
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")


# set of REST endpoints


@app.get("/books/")
def get_books():
    return get_all_books()


@app.get("/book/{isbn}")
def get_book_by_isbn(isbn: int):
    return get_by_isbn(isbn)


@app.get("/book/year/{year}")
def get_books_by_year(year: int):
    return get_by_year(year)


@app.get("/book/author/{author}")
def get_books_by_author(author: str):
    return get_by_author(author)


@app.post("/book/")
def store_book(book: Book):
    return put_book_to_storage(book)
