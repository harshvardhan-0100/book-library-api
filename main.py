from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(): 
    return {"message": "Book Library API is running"}