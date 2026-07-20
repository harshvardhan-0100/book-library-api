from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

app = FastAPI()

# This defines what a "book" looks like in our API
class Book(BaseModel):
    title: str               # required — must be text
    author: str              # required — must be text
    status: str = "unread"   # optional — defaults to "unread" if not provided
    rating: Optional[int] = None  # optional — a number from 1-5, or nothing

# Temporary in-memory storage
books_db = {}

@app.post("/books", status_code=201)
def add_book(book: Book):
    book_id = str(uuid4())
    books_db[book_id] = {"id": book_id, **book.model_dump()}
    return books_db[book_id]