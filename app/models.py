from typing import List

import strawberry
from pydantic import BaseModel


class Book(BaseModel):
    isbn: int
    title: str
    author: list
    year: int


@strawberry.type
class G_Book:
    isbn: int
    title: str
    author: List[str]
    year: int
