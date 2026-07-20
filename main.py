from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# This defines what a "book" looks like in our API
class Book(BaseModel):
    title: str               # required — must be text
    author: str              # required — must be text
    status: str = "unread"   # optional — defaults to "unread" if not provided
    rating: Optional[int] = None  # optional — a number from 1-5, or nothing