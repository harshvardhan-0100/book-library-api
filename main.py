from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4

app = FastAPI()

@app.get("/")
def root(): 
    return {"message": "Book Library API is running"}