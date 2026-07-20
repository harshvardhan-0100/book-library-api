from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4
from enum import Enum

class StatusEnum(str, Enum):
    unread = "unread"
    reading = "reading"
    finished = "finished"
    wishlisted = "wishlisted"

app = FastAPI()

# This defines what a "book" looks like in our API
class Book(BaseModel):
    title: str                               # required — must be text
    author: str                              # required — must be text
    status: StatusEnum = StatusEnum.unread   # optional — defaults to "unread" if not provided
    rating: Optional[float] = None           # optional — a number from 1-5, or nothing

# Temporary in-memory storage
books_db = {}

# POST endpoint
@app.post("/books", status_code=201)
def add_book(book: Book):
    book_id = str(uuid4())
    books_db[book_id] = {"id": book_id, **book.model_dump()}
    return books_db[book_id]

# GET endpoint
@app.get("/books")
def get_all_books():
    return list(books_db.values())

# GET/books/{id} endpoint (reading one book)
@app.get("/books/{book_id}")
def get_book(book_id: str):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id]

# POST /books endpoint
@app.put("/books/{book_id}")
def update_book(book_id: str, updated_book: Book):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[book_id] = {"id": book_id, **updated_book.model_dump()}
    return books_db[book_id]